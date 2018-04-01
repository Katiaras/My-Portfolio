using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
using System.Linq;
using System.Web;

namespace AubgBank.Models
{
    public class Client
    {
        [Key]
        [DatabaseGenerated(DatabaseGeneratedOption.Identity)]
        public int ID { get; set; }

        [Required(ErrorMessage ="First Name is Required!")]
        [Display(Name="First Name")]
        public string Firstname { get; set; }

        [Required(ErrorMessage = "Last Name is Required!")]
        [Display(Name = "Last Name")]
        public string Lastname { get; set; }

        [Required(ErrorMessage = "Email is Required!")]
        [EmailAddress(ErrorMessage ="Please Enter a Valid Email!")]
        public string Email { get; set; }

        [Required(ErrorMessage = "Date of Birth is Required!")]
        [DisplayFormat(DataFormatString = "{0: dd/MM/yyyy}", ApplyFormatInEditMode = true)]
        [Display(Name = "Date Of Birth")]
        public DateTime DateOfBirth { get; set; }

        public string Gender { get; set; }

        public string Country { get; set; }

    }
    
}