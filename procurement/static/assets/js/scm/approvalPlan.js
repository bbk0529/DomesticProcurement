$(function(){


    $('#delete').click(function(){
        console.log("delete click");
        console.log( $("input[name='SA_No']").val())
        $.ajax({
            url:"deleteRecord",
            type:"POST",
            data :{
                'csrfmiddlewaretoken': '{{csrf_token}}',
                'SA_No' : $("input[name='SA_No']").val(),
            },
            success:function(data){
                 // location.reload();


                $('#header').html(''+
                '<div class="sufee-alert alert with-close alert-secondary alert-dismissible fade show" id="alert_message">'+
                    '<span class="badge badge-pill badge-primary">Success</span>'+
                    'Assay No : ' +
                     $("input[name='SA_No']").val() +
                        ' Change has been successfully deleted.'+
                      '<button type="button" class="close" data-dismiss="alert" aria-label="Close">'+
                        '<span aria-hidden="true">&times;</span>'+
                    '</button>'+
                '</div>'
                  )
                window.setTimeout(function() {
                    $("#alert_message").fadeTo(300, 0).slideUp(300, function(){
                      $(this).remove();
                    });
                }, 1000);
                 window.location.reload();
                if($('#radio_create').is(':checked')) {
                    ///////////////////////////////////

                }
            },
            error :function(){
                $('#header').html(''+
                '<div class="sufee-alert alert with-close alert-danger alert-dismissible fade show" id="alert_message">'+
                    '<span class="badge badge-pill badge-danger">Failure</span>'+
                        'delete has NOT been successfully done'+
                      '<button type="button" class="close" data-dismiss="alert" aria-label="Close">'+
                        '<span aria-hidden="true">&times;</span>'+
                    '</button>'+
                '</div>'
                )
                window.setTimeout(function() {
                    $("#alert_message").fadeTo(300, 0).slideUp(300, function(){
                      $(this).remove();
                    });
                }, 2000);
            }
        })

    })

    $('#save').click(function(){
      console.log("save clicked");
      $.ajax({
          url:"updateQuery",
          type:"POST",
          data:{
              'csrfmiddlewaretoken': '{{csrf_token}}',
              'Category': $('#changeDocOptions').val(),
              'SA_No' : $("input[name='SA_No']").val(),
              'Type' : $("input[name='Type']").val(),
              'Date' : $("input[name='Date']").val(),
              'Number_of_suppliers' : $("input[name='Number_of_suppliers']").val(),
              'Details_1' : $("textarea[name='Details_1']").val(),
              'Details_2' : $("textarea[name='Details_2']").val(),
              'Description' : $.trim($("textarea[name='Description']").val()),
              'Supplier1'                                  :   $("#Supplier1").text(),
              'Supplier1_Qty'                              :   $("#Supplier1_Qty").text(),
              'Supplier1_Final_Unit_Price'                 :   $("#Supplier1_Final_Unit_Price").text(),
              'Supplier1_Fabricating_Goods'                :   $("#Supplier1_Fabricating_Goods").val(),
              'Supplier1_Modification_of_free_offerd_item' :   $("#Supplier1_Modification_of_free_offerd_item").val(),

              'Supplier2'                                  :   $("#Supplier2").text(),
              'Supplier2_Qty'                              :   $("#Supplier2_Qty").text(),
              'Supplier2_Final_Unit_Price'                 :   $("#Supplier2_Final_Unit_Price").text(),
              'Supplier2_Fabricating_Goods'                :   $("#Supplier2_Fabricating_Goods").val(),
              'Supplier2_Modification_of_free_offerd_item' :   $("#Supplier2_Modification_of_free_offerd_item").val(),

              'Supplier3'                                  :   $("#Supplier3").text(),
              'Supplier3_Qty'                              :   $("#Supplier3_Qty").text(),
              'Supplier3_Final_Unit_Price'                 :   $("#Supplier3_Final_Unit_Price").text(),
              'Supplier3_Fabricating_Goods'                :   $("#Supplier3_Fabricating_Goods").val(),
              'Supplier3_Modification_of_free_offerd_item' :   $("#Supplier3_Modification_of_free_offerd_item").val(),

              'Supplier4'                                  :   $("#Supplier4").text(),
              'Supplier4_Qty'                              :   $("#Supplier4_Qty").text(),
              'Supplier4_Final_Unit_Price'                 :   $("#Supplier4_Final_Unit_Price").text(),
              'Supplier4_Fabricating_Goods'                :   $("#Supplier4_Fabricating_Goods").val(),
              'Supplier4_Modification_of_free_offerd_item' :   $("#Supplier4_Modification_of_free_offerd_item").val(),

              'Supplier5'                                  :   $("#Supplier5").text(),
              'Supplier5_Qty'                              :   $("#Supplier5_Qty").text(),
              'Supplier5_Final_Unit_Price'                 :   $("#Supplier5_Final_Unit_Price").text(),
              'Supplier5_Fabricating_Goods'                :   $("#Supplier5_Fabricating_Goods").val(),
              'Supplier5_Modification_of_free_offerd_item' :   $("#Supplier5_Modification_of_free_offerd_item").val(),

              'Supplier6'                                  :   $("#Supplier6").text(),
              'Supplier6_Qty'                              :   $("#Supplier6_Qty").text(),
              'Supplier6_Final_Unit_Price'                 :   $("#Supplier6_Final_Unit_Price").text(),
              'Supplier6_Fabricating_Goods'                :   $("#Supplier6_Fabricating_Goods").val(),
              'Supplier6_Modification_of_free_offerd_item' :   $("#Supplier6_Modification_of_free_offerd_item").val(),


              'Supplier7'                                  :   $("#Supplier7").text(),
              'Supplier7_Qty'                              :   $("#Supplier7_Qty").text(),
              'Supplier7_Final_Unit_Price'                 :   $("#Supplier7_Final_Unit_Price").text(),
              'Supplier7_Fabricating_Goods'                :   $("#Supplier7_Fabricating_Goods").val(),
              'Supplier7_Modification_of_free_offerd_item' :   $("#Supplier7_Modification_of_free_offerd_item").val(),


              'Supplier8'                                  :   $("#Supplier8").text(),
              'Supplier8_Qty'                              :   $("#Supplier8_Qty").text(),
              'Supplier8_Final_Unit_Price'                 :   $("#Supplier8_Final_Unit_Price").text(),
              'Supplier8_Fabricating_Goods'                :   $("#Supplier8_Fabricating_Goods").val(),
              'Supplier8_Modification_of_free_offerd_item' :   $("#Supplier8_Modification_of_free_offerd_item").val(),
          },
          success:function(data){
               // location.reload();


              $('#header').html(''+
              '<div class="sufee-alert alert with-close alert-secondary alert-dismissible fade show" id="alert_message">'+
                  '<span class="badge badge-pill badge-primary">Success</span>'+
                  'Assay No : ' +
                   $("input[name='SA_No']").val() +
                      ' Change has been successfully saved.'+
                    '<button type="button" class="close" data-dismiss="alert" aria-label="Close">'+
                      '<span aria-hidden="true">&times;</span>'+
                  '</button>'+
              '</div>'
                )
              window.setTimeout(function() {
                  $("#alert_message").fadeTo(300, 0).slideUp(300, function(){
                    $(this).remove();
                  });
              }, 2000);
              if($('#radio_create').is(':checked')) {
                  ///////////////////////////////////

              }
          },
          error :function(){
              $('#header').html(''+
              '<div class="sufee-alert alert with-close alert-danger alert-dismissible fade show" id="alert_message">'+
                  '<span class="badge badge-pill badge-danger">Failure</span>'+
                      'Change has NOT been successfully saved. SA Number is not given or server is not working properly'+
                    '<button type="button" class="close" data-dismiss="alert" aria-label="Close">'+
                      '<span aria-hidden="true">&times;</span>'+
                  '</button>'+
              '</div>'
              )
              window.setTimeout(function() {
                  $("#alert_message").fadeTo(300, 0).slideUp(300, function(){
                    $(this).remove();
                  });
              }, 2000);
          }

      })
    }) // end of save




    $('#radio_create').click(function(){
      console.log('clicked radio_create')
      $('#newDocOptions').prop('hidden',false)
      $('#changeDocOptions').prop('hidden',true)

      $.ajax({
        url : "approvalPlanCreate",
        type : "GET",
        success : function(data) {
            console.log("successfully communicated with Server");
            $("#approvalPlanQuery").html(
              data
            );
        }
      })
    })
    function query(assayNo){
        if (assayNo!='') {
            $('#radio_change').prop('checked', true)
            $('#changeDocOptions').prop('hidden', false);
            $('#newDocOptions').prop('hidden', true);
            console.log(assayNo);
            $.ajax({
                url : "approvalPlanQuery",
                type : "GET",
                data: {
                    'SA_No' : assayNo
                },
                success : function(data) {
                    console.log("successfully communicated with Server");
                    $("#approvalPlanQuery").html(
                      data
                    );
                }
            }) //end of $.ajax
        }
    }

    // key press to search
    $("#assayNo").keypress(function(event) {
        if (event.keyCode === 13) {
            console.log('enter key in')
            var assayNo=$("#assayNo").val()
            query(assayNo)
        }
    });


    $('#query').click(function(){
      console.log("clicked//")
      var assayNo=$("#assayNo").val()
      query(assayNo)
    });
} ) //end of function
