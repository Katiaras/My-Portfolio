using System;
using System.Collections.Generic;
using System.Data;
using System.Data.Entity;
using System.Diagnostics;
using System.Linq;
using System.Net;
using System.Web;
using System.Web.Mvc;
using Your_Tunes.Models;

namespace Your_Tunes.Controllers
{
    public class ShoppingCartController : Controller
    {
        private SongsDBContext db = new SongsDBContext();
        // GET: ShoppingCart
        public ActionResult Index(string List)
        {
            if (!String.IsNullOrEmpty(List))
            {
                // Take all entries
                var songs = from a in db.Songs
                            select a;
                List<Song> shopping_list = new List<Song>();
                // Get the shopping list
                var shopping_id_list = List.Split(',');
                var int_shopping_id_list = Array.ConvertAll(shopping_id_list, s => Int32.Parse(s));
                Debug.WriteLine(int_shopping_id_list);

                songs = songs.Where(s => int_shopping_id_list.Contains(s.SongId));

                return View(songs);
            }
            else
            {
                return View();
            }
        }

        // GET: Checkout
        [Authorize]
        public ActionResult Checkout()
        {
            return View();
        }
    }
}