$(function(){

        $('[id*=gouvernorat_').on('click',function(){


            let gouvernorat = $(this);
            let allgouvernorat = $('[id*=gouvernorat_');
            let gouvernoratId = $(this)["0"].id;
            allgouvernorat.css("fill", "white");
            gouvernorat.css("fill","#4527A0")

           
        });
})

