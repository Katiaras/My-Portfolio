using System.ComponentModel.DataAnnotations;
using Nop.Web.Framework.Mvc.ModelBinding;
using Nop.Web.Framework.Mvc.Models;

namespace Nop.Plugin.Widgets.HomePageNewProducts.Models
{
    public class ConfigurationModel : BaseNopModel
    {
        public int ActiveStoreScopeConfiguration { get; set; }
        
        [NopResourceDisplayName("Plugins.Widgets.HomePageNewProducts")]
        [UIHint("Specify the Number Of Products To Be Shown")]
        public int NumberOfProducts { get; set; }
        public bool NumberOfProducts_OverrideForStore { get; set; }
        
    }
}