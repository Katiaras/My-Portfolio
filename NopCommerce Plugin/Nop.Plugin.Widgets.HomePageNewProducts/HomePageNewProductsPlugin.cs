using System.Collections.Generic;
using System.IO;
using Nop.Core;
using Nop.Core.Plugins;
using Nop.Services.Cms;
using Nop.Services.Configuration;
using Nop.Services.Localization;
using Nop.Services.Media;

namespace Nop.Plugin.Widgets.HomePageNewProducts
{

    /// <summary>
    /// PLugin
    /// </summary>
    public class HomePageNewProductsPlugin : BasePlugin, IWidgetPlugin
    {
        private readonly IPictureService _pictureService;
        private readonly ISettingService _settingService;
        private readonly IWebHelper _webHelper;

        public HomePageNewProductsPlugin(IPictureService pictureService,
            ISettingService settingService, IWebHelper webHelper)
        {
            this._pictureService = pictureService;
            this._settingService = settingService;
            this._webHelper = webHelper;
        }

        /// <summary>
        /// Gets widget zones where this widget should be rendered
        /// </summary>
        /// <returns>Widget zones</returns>
        public IList<string> GetWidgetZones()
        {
            return new List<string> { "home_page_top" };
        }

        /// <summary>
        /// Gets a configuration page URL
        /// </summary>
        public override string GetConfigurationPageUrl()
        {
            return _webHelper.GetStoreLocation() + "Admin/WidgetsHomePageNewProducts/Configure";
        }

        /// <summary>
        /// Gets a view component for displaying plugin in public store
        /// </summary>
        /// <param name="widgetZone">Name of the widget zone</param>
        /// <param name="viewComponentName">View component name</param>
        public void GetPublicViewComponent(string widgetZone, out string viewComponentName)
        {
            viewComponentName = "WidgetsHomePageNewProducts";
        }

        /// <summary>
        /// Install plugin
        /// </summary>
        public override void Install()
        {
            //settings
            var settings = new HomePageNewProductsSettings
            {
                // default 4 items
                NumberOfProducts = 4

            };
            _settingService.SaveSetting(settings);



            this.AddOrUpdatePluginLocaleResource("Plugins.Widgets.HomePageNewProducts.NumberOfProducts", "Number Of Products: ");
            this.AddOrUpdatePluginLocaleResource("Plugins.Widgets.HomePageNewProducts.NumberOfProducts.Hint", "Specify the number of Products to be shown");

            base.Install();
        }

        /// <summary>
        /// Uninstall plugin
        /// </summary>
        public override void Uninstall()
        {
            //settings
            _settingService.DeleteSetting<HomePageNewProductsSettings>();

            //locales

            this.DeletePluginLocaleResource("Plugins.Widgets.HomePageNewProducts.NumberOfProducts");
            this.DeletePluginLocaleResource("Plugins.Widgets.HomePageNewProducts.NumberOfProducts.Hint");


            base.Uninstall();
        }
    }
}