<script>
$( document ).ready(function() {
    console.log("Document Loaded");});        
</script>



<script>
$(document).on('submit','form',function(event){ //looks for any form on page that is submitted
event.preventDefault(); // Stop form from submitting normally

// Get some values from elements on the page:
var $form = $( this ); //loads all data from form into parent variable
var form_id = $form.attr('id'); //find the ID of the submitted form
    console.log(form_id); //for testing
var url = $form.attr( "action" ); //for  flask to know what URL is associated with POST  
    console.log(url);              

if (form_id == 'remove'){
        console.log("This is the remove function");
    var myCheckboxes = new Array();
    $form.find( "input[name='rowID']:checked" ).each(function() {
            myCheckboxes.push($(this).val());
            $(this).prop("checked", false)});
    var data = {'function':form_id ,'removeRows': myCheckboxes}                      
} 
else if (form_id == 'add') {
        console.log("This is the add function");
    //var arch = $( "select#arch option:checked" ).val();
    var arch = $('#metaID').data();
        console.log(arch)
    var dataString = $form.serializeArray()
        console.log(dataString)
    var data = {'function':form_id ,'addRow': dataString, 'arch':arch}
} 
else if (form_id == 'eventAdd') {
        console.log("This is the eventAdd function");

    var dataString = $form.serializeArray()
        console.log(dataString)
    var data = {'function':form_id ,'addRow': dataString}
}                      
$.ajax({
        url: url,
        contentType: 'application/json',
        dataType : 'json',
        data: JSON.stringify(data),
        type: 'POST',
        timeout: 10000,
        success: function(response){
            console.log(response)
            $form.find("input[type=text], textarea").val("");
            location.reload();
            
        },
        error: function(jqXHR, textStatus, errorThrown){
            console.log(textStatus);
            //document.getElementById('display').innerHTML = textStatus;
        }
    });               

return false; //not sure why this is needed, maybe saying if no ajax post then do nothing
});

</script>