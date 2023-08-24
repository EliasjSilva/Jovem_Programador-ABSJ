// Keyboard Event

$(document).ready(function(){
        $(document).keydown(function(e){
                //console.log(e.key)
                if(e.key === 's'){
                        $('.div1').animate({
                                'top': '+=20px'
                        })
                }else if(e.key === 'w'){
                        $('.div1').animate({
                                'top': '-=20'
                        })
                }else if(e.key === 'd'){
                        $('.div1').animate({
                                'left': '+=20'
                        })
                }else if(e.key === 'a'){
                        $('.div1').animate({
                                'left': '-=20'
                        })
                }
                
        })
})