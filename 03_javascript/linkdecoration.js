// Exercise 2.3 Javascript file  //
// Read the instructions.html //

//some helpful debug code

$("#javascript_start").html("[OK] Started executing the javascript file");
$("#javascript_end").html("[WAITING]...this far we haven't reached the end... Maybe you should try FireBug?");

// ADD YOUR CODE BETWEEN THESE LINES //
/*$("a").each(function(i,l) {
    //Do your work
    $( "li" ).filter( ".pdf" ).css( "background-color", "red" );

      console.log("sdasdsadsa");
    //  alert( "Index #" + i + ": " + l );
});*/
$(document).ready(function() {
    $("a[href$='.pdf']").addClass("pdf");
    });

    $(document).ready(function() {
          $("a").filter(function() {
           return this.hostname && this.hostname !== location.hostname;
         }).addClass('external');
        });

        $(document).ready(function() {
            $("a[href$='.zip']").addClass("download");
            });

          /*  $(document).ready(function() {
                  $("a").filter(function() {
                   return this.hostname && this.hostname !== location.hostname;
                 }).addClass('note');
               });*/



// ADD YOUR CODE BETWEEN THESE LINES //

//some helpful debug code

$("#javascript_end").html("[OK] The end of your javascript file was reached. (meaning there were no huge errors) Hopefully your code works too! ");
