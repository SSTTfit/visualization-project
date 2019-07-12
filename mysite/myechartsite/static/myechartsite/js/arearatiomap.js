
var barViz=(function ($) {
    var _self = {},
        time,
        disease,
        chooseData={},
        //colors = ["334d5c","45b29e","efc94c","e27a3f","df4949","aeaeae","776355","57385c","4edaef","8db500"]
        radioTemplate = '<div class="radioItem"><input type="radio" name="Disease" class="radio"><label></label></div>',
        //  radioTemplate='<input type="radio" name="Disease" class="radio"><label class="control"></label><br>',
        buttonTemplate='<div class="buttonItem"><input type="button" class="btn-year normal"></div>';
    //radioCss={background:'#e5e9f2',width:'100%'};

    function  initControl() {
        //设置疾病单选框
        $.each(disease, function(index){
            var snippet = $(radioTemplate);
            if (index==0) {
                snippet.find('label').text(this[0]).attr('for',this[0]).end()
                    .find('.radio').attr('value',this[1]).attr('checked','checked').attr('id',this[0]).end()
                    .appendTo("#disease_choose");
                //console.log(this);
            }else
            {
                snippet.find('label').text(this[0]).attr('for',this[0]).end()
                    .find('.radio').attr('value',this[1]).attr('id',this[0]).end()
                    .appendTo("#disease_choose");
            }
        });
        //设置单选框样式
        //$('.radioItem').find('label').css(radioCss).css({"border-radius":'5px',"margin-bottom":'6px'});
        //设置年份按钮
        //var max=Math.max.apply(null,time);var min=Math.min.apply(null,time);$("#time").attr("max",max).attr("min",min).attr("step",1);
        //console.log(max);
        $.each(time,function (index) {
            var sample=$(buttonTemplate);
            if(index==0){
                sample.find(':button').attr("value",this).attr("id",this).addClass('selected').removeClass('normal').end()
                    .appendTo("#right_col");
            }
            else if(index%2==1){
                sample.find(':button').attr("value",this).attr("id",this).end()
                    .appendTo("#left_col");
            }else
            {
                sample.find(':button').attr("value",this).attr("id",this).end()
                    .appendTo("#right_col");
            }
        });
        //设置按钮样式
        $(".buttonItem").css({"margin-bottom":'8px'});
        rebtSkin();
        //$(".b").css({});
    }
    function loadData() {
        $.ajax({
            url: '/myechartsite/index_expert/arearatiomap_data',
            type: 'GET',
            dataType: 'json',
            success: function (data) {
                disease=data.disease;
                time=data.time;
                chooseData.ch_disease=disease[0][1];
                chooseData.ch_year=time[0];
                initControl();
            }
        });
    }

    function reData() {
        $('#main')[0].contentWindow.filterBy(chooseData.ch_disease,chooseData.ch_year);
        console.log(chooseData);
    }
    function rebtSkin() {

        $(".selected").css({"background":'#b558f6',"color":'#ffffff'});
        $(".normal").css({"background":'#e5e9f2',"color":'#748aa1'})
    }
    function initEvents() {

        //监听单选框
        $("#disease_choose").on('click',':radio',function() {
            chooseData.ch_disease=$(this).val();
            //chooseData=wholeData[$("input[type='radio']:checked").val()];
            //alert(chooseData.ch_disease);
            $('#disease_span').text($(this).attr('id'));
            console.log($(this).attr('id'));
            reData();
        });
        //监听年份按钮
        $("#year_choose").on('click',':button',function (event) {
            var chooseDom=event.target;
            chooseData.ch_year= chooseDom.getAttribute('value');//获取指定的元素
            $('#year_span').text($(this).val());
            //console.log(chooseData.ch_year);
            reData();
            $.each($(".btn-year"),function () {
                //  if($(this).hasClass("normal")){
                $(this).removeClass("selected").addClass("normal");
                //  }
            });
            $(this).addClass("selected").removeClass("normal");
            rebtSkin();
        });

        $(".btn-group").on('click','.btn',function () {
            $.each($(".btn"),function () {
                //  if($(this).hasClass("normal")){
                $(this).removeClass("select-btn");
                //  }
            });
            $(this).addClass("select-btn");
        });
    }
    _self.init = function () {
        loadData();
        initEvents();
    };
    return _self;
}(jQuery));
jQuery(document).ready(function(){
    barViz.init();
    //PointerEventsPolyfill.initialize({});
});
