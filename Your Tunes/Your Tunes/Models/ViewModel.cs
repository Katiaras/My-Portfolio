using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace Your_Tunes.Models
{
    // Used for Categories and DB data
    public class ViewModel
    {
        public IEnumerable<Song> Songs { get; set; }
        public IEnumerable<string> Categories { get; set; }

    }
}