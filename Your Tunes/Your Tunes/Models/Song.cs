using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace Your_Tunes.Models
{
    public class Song
    {

        public int SongId { get; set; }
        public string Title { get; set; }
        public string Album { get; set; }
        public string Singer { get; set; }
        public string Category { get; set; }

        [System.ComponentModel.DisplayName("Year of Release")]
        public int YearOfRelease { get; set; }
        public float Price { get; set; }
        public string Description { get; set; }
        public string TrimedDescription
        {
            get
            {
                const int MAX_LENGTH = 20;
                if (this.Description == null || this.Description == "")
                {
                    return "There is no description";
                }
                else if (this.Description.Length > MAX_LENGTH)
                {
                    return this.Description.Substring(0, 17) + "...";
                }

                return this.Description;
            }

        }

    }

}