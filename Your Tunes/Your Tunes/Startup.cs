using Microsoft.Owin;
using Owin;

[assembly: OwinStartupAttribute(typeof(Your_Tunes.Startup))]
namespace Your_Tunes
{
    public partial class Startup
    {
        public void Configuration(IAppBuilder app)
        {
            ConfigureAuth(app);
        }
    }
}
