$(function(){
      $('#check').click(function(){
          var assayNo=$("#assayNo").val()
          query(assayNo)
      }); //end of #check click

      $("#assayNo").keypress(function(event) {
          if (event.keyCode === 13) {
              console.log('enter key in')
              var assayNo=$("#assayNo").val()
              query(assayNo)
          }
      });

      function query(assayNo){
      $.ajax({
              url : "assayQuery",
              type : "get",
              data: {
                'SA_No' : assayNo
                },
            // async: false,
            success : function(data) {
                console.log("successfully communicated with Server");
                // console.log(data);

                $("#result").html(data);
                $('textarea').each(function () {

                    height=this.scrollHeight
                   this.setAttribute('style', 'height:' + (height) + 'px;overflow-y:hidden;');
                   // this.setAttribute('style', 'overflow-y:hidden;');
                }).on('input', function () {
                  this.style.height = 'auto';
                  this.style.height = (this.scrollHeight) + 'px';
                });



            },
            error: function(){
                console.log("error")
                alert('The requested partNo is not seachable. Please register new partnr');
            }
        }) //end of $.ajax
    }




  });
