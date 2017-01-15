using Microsoft.Owin;
using Owin;

[assembly: OwinStartupAttribute(typeof(tc_and_octo.Startup))]
namespace tc_and_octo
{
    public partial class Startup {
        public void Configuration(IAppBuilder app) {
            ConfigureAuth(app);
        }
    }
}
