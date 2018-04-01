using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
using System.Linq;
using System.Web;

namespace AubgBank.Models
{
    public class Service
    {
        [Key]
        [DatabaseGenerated(DatabaseGeneratedOption.Identity)]
        public int ServiceID { get; set; }

        [Required(ErrorMessage = "Loan Service Name is Required!")]
        [Display(Name = "Loan Service Name")]
        public string LoanServiceName { get; set; }

        [Required(ErrorMessage = "Please Enter an Upper Limit for the Loan")]
        [Display(Name = "Loan Upper Limit")]
        public int LoanLimit { get; set; }

        [Required(ErrorMessage = "Interest Rate is Required!")]
        public double InterestRate { get; set; }


        [Required(ErrorMessage = "The Due Date for the Loan is Required! (Date Format Hint: dd/mm/yyyy)")]
        [DisplayFormat(DataFormatString = "{0: dd/MM/yyyy}", ApplyFormatInEditMode = true)]
        [Display(Name = "Maturity Date")]
        public DateTime MaturityDate { get; set; }

        [DataType(DataType.MultilineText)]
        [StringLength(100, MinimumLength =10)]
        [MaxLength(100, ErrorMessage ="The Limit for the Description is 100 letters")]
        public string Description { get; set; }
        
    }
}