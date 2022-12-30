function printEl(){
    var body = $('body').html(),
        element = $('.print');
    $('body').html(element);
    window.print();
    $('body').html(body);
}