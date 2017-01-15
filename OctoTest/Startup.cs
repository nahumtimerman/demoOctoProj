using Microsoft.Owin;
using Owin;

[assembly: OwinStartupAttribute(typeof(OctoTest.Startup))]
namespace OctoTest
{
    public partial class Startup
    {
        public void Configuration(IAppBuilder app)
        {
            ConfigureAuth(app);
        }
    }
}
