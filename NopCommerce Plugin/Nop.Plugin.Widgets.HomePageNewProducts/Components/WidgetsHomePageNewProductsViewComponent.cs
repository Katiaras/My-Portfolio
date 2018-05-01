using Microsoft.AspNetCore.Mvc;
using Nop.Core;
using Nop.Core.Caching;
using Nop.Plugin.Widgets.HomePageNewProducts.Models;
using Nop.Services.Configuration;
using Nop.Services.Media;
using Nop.Web.Framework.Components;
using System.Linq;
using Nop.Core.Domain.Catalog;
using Nop.Services.Catalog;
using Nop.Services.Orders;
using Nop.Services.Security;
using Nop.Services.Stores;
using Nop.Web.Factories;
using Nop.Web.Infrastructure.Cache;

namespace Nop.Plugin.Widgets.HomePageNewProducts.Components
{
    [ViewComponent(Name = "WidgetsHomePageNewProducts")]
    public class WidgetsHomePageNewProductsViewComponent : NopViewComponent
    {
        private readonly IStoreContext _storeContext;
        private readonly IStaticCacheManager _cacheManager;
        private readonly ISettingService _settingService;
        private readonly IPictureService _pictureService;
        private readonly CatalogSettings _catalogSettings;
        private readonly IProductModelFactory _productModelFactory;
        private readonly IProductService _productService;
        private readonly IAclService _aclService;
        private readonly IStoreMappingService _storeMappingService;
        private readonly IOrderReportService _orderReportService;

        public WidgetsHomePageNewProductsViewComponent(
            CatalogSettings catalogSettings,
            IStoreContext storeContext, 
            IStaticCacheManager cacheManager, 
            ISettingService settingService, 
            IPictureService pictureService,
            IProductModelFactory productModelFactory,
            IProductService productService,
            IAclService aclService,
            IStoreMappingService storeMappingService,
            IOrderReportService orderReportService)
        {
            this._storeContext = storeContext;
            this._cacheManager = cacheManager;
            this._settingService = settingService;
            this._pictureService = pictureService;
            this._catalogSettings = catalogSettings;
            this._productModelFactory = productModelFactory;
            this._productService = productService;
            this._storeContext = storeContext;
            this._aclService = aclService;
            this._storeMappingService = storeMappingService;
            this._orderReportService = orderReportService;
            this._cacheManager = cacheManager;
        }

        public IViewComponentResult Invoke(string widgetZone, object additionalData)
        {
            
            // Loading the seting value
            var homePageSettings = _settingService.LoadSetting<HomePageNewProductsSettings>(_storeContext.CurrentStore.Id);
            int NumberOfProducts = homePageSettings.NumberOfProducts;


            //load and cache report
            var report = _cacheManager.Get(string.Format(ModelCacheEventConsumer.HOMEPAGE_BESTSELLERS_IDS_KEY, _storeContext.CurrentStore.Id),
                () => _orderReportService.BestSellersReport(
                        storeId: _storeContext.CurrentStore.Id)
                    .ToList());

            //load products
            var products = _productService.GetProductsByIds(report.Select(x => x.ProductId).ToArray());

            //ACL and store mapping
            products = products.Where(p => _aclService.Authorize(p) && _storeMappingService.Authorize(p)).ToList();
            //Order by MarkAsNewStartDate Descending, in order to get the newest first 
            // Then get the first NumberOfProducts Specified in the Settings
            // Getting the first ones guarantees that they are the Newest
            products = products.OrderByDescending(p => p.MarkAsNewStartDateTimeUtc).Take(NumberOfProducts).ToList();
            
            //prepare model
            var model = _productModelFactory.PrepareProductOverviewModels(products, true, true).ToList();
            return View("~/Plugins/Widgets.HomePageNewProducts/Views/PublicInfo.cshtml", model);
        }
        
    }
}
