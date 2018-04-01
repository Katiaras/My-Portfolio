using System;
using System.Collections.Generic;
using System.Data;
using System.Data.Entity;
using System.Linq;
using System.Net;
using System.Web;
using System.Web.Mvc;
using Your_Tunes.Models;

namespace Your_Tunes.Controllers
{
    public class HomeController : Controller
    {
        private SongsDBContext db = new SongsDBContext();
        
        public ActionResult Index()
        {
            ViewModel viewData = new ViewModel();

            // Take all entries
            viewData.Songs = from a in db.Songs
                        select a;
            // Shuffle Them
            var randomOrdering = viewData.Songs.OrderBy(o => Guid.NewGuid());

            // Get the top (?) from the shuffled collection 
            viewData.Songs = (from song in randomOrdering
                         select song).Take(6);

            // Store Unique Categories
            viewData.Categories = (from a in db.Songs
                                  select a.Category).Distinct();

            //Console.WriteLine(viewData.Categories);
            
            return View(viewData);
        }

        public ActionResult About()
        {
            ViewBag.Message = "Your application description page.";

            return View();
        }

        public ActionResult Contact()
        {
            ViewBag.Message = "Your contact page.";

            return View();
        }
    }
}