using Microsoft.Owin;
using Owin;

[assembly: OwinStartupAttribute(typeof(AubgBank.Startup))]
namespace AubgBank
{
    public partial class Startup
    {
        public void Configuration(IAppBuilder app)
        {
            ConfigureAuth(app);
        }
    }
}
