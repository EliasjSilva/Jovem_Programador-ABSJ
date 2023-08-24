$(document).ready(function(){
// Functions  Hide and Show
        $('.hide').click(function(){
                $('.p1').fadeOut(1000)
        })
        $('.show').dblclick(function(){ // DoubleClick -- dblclick
                $('.p1').fadeIn('slow')
        })

// Function toggle
        $('.t1').click(function(){
                $('.p2').fadeToggle(1500)
        })  

//Function Slide
        //$('.div1').hide()
        $('.t3').click(function(){
                $('.div1').slideToggle() // to SlideDown to bottom, to slideUp to top and slideToggle for both.
        })

//Open another window
        $('.btn').click(function(){
                (window).open('eventosMouse.html')
        })

//Mouse enter
        $('.div2').mouseenter(function(){
                $(this).css({'background-color': 'white' , 'color': 'black', 'border-radius': '50%' , 'width': '+=100px' , 'height': '+=150px'}).text('The mouse entered!')
        })
        $('.div2').mouseleave(function(){
                $(this).css({'background-color':'black', 'color': 'white'}).text('The mouse left!')
        })
        
}) 