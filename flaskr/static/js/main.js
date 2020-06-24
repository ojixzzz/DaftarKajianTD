$(function(){
    $("#form-register").validate();
    $("#form-total").steps({
        headerTag: "h2",
        bodyTag: "section",
        transitionEffect: "fade",
        enableAllSteps: true,
        stepsOrientation: "vertical",
        autoFocus: true,
        transitionEffectSpeed: 500,
        titleTemplate : '<div class="title">#title#</div>',
        onStepChanging: function (event, currentIndex, newIndex)
        {
            $("#form-register").validate().settings.ignore = ":disabled,:hidden";
            return $("#form-register").valid();
        },
        labels: {
            previous : 'Back Step',
            next : '<i class="zmdi zmdi-arrow-right"></i>',
            finish : '<i class="zmdi zmdi-check"></i>',
            current : ''
        },
        onFinished: function (event, currentIndex) {
            $("#form-register").submit();
        }
    })
});
