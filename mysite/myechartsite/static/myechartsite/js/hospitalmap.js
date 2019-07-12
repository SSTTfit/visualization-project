
var barViz=(function ($) {
    var _self = {},
        Province,
        Citys,
        Level,
        Features,
        chooseData={},
        //colors = ["334d5c","45b29e","efc94c","e27a3f","df4949","aeaeae","776355","57385c","4edaef","8db500"]
        selectTemplate = '<option></option>';
        //  radioTemplate='<input type="radio" name="Disease" class="radio"><label class="control"></label><br>',
        //buttonTemplate='<div class="buttonItem"><input type="button" class="btn-year normal"></div>';
    //radioCss={background:'#e5e9f2',width:'100%'};

    function  initControl() {
        //设置省份下拉框
        $.each(Province, function(index){
            var snippet = $(selectTemplate);
                snippet.text(this).attr('value',this)
                    .appendTo("#province");
        });
        /*此刻先不设置城市下拉框，确定省份之后再决定*/
        //设置等级和特色专科下拉框
        $.each(Level,function (index) {
            var snippet = $(selectTemplate);
            snippet.text(this).attr('value',this)
                .appendTo("#level");
        });
        $.each(Features,function (index) {
            var snippet = $(selectTemplate);
            snippet.text(this).attr('value',this)
                .appendTo("#features");
        });
    }
    function initCitys(p) {
        var initial='<option value="all">城市</option>';
        //清空原来
        if(p!=null) {
            $("#city").empty();
            $('#city').append(initial);
            $.each(p, function () {
                var snippet = $(selectTemplate);
                snippet.text(this).attr('value', this)
                    .appendTo("#city");
            });
        }else {
            $("#city").empty();
            $('#city').append(initial);
        }
    }
    function loadData() {
        $.ajax({
            url: '/myechartsite/index_customer/hospitalmap_data',
            type: 'GET',
            dataType: 'json',
            success: function (data) {
                Province=data.province;
                Citys=data.city;
                Level=data.level;
                Features=data.features;
                chooseData={
                    ch_province:'all',
                    ch_city:'all',
                    ch_level:'all',
                    ch_feature:'all'
                };
                initControl();
            }
        });
    }
    function reData() {
        $('#main')[0].contentWindow.filterBy(chooseData.ch_province,chooseData.ch_city,chooseData.ch_level,chooseData.ch_feature);
        console.log(chooseData);
    }
    function initEvents() {

        //监听省份下拉框，并填充城市内容
        $("#province").change(function() {
            chooseData.ch_province = $(this).val();
            if($(this).val()!="all") {
                //chooseData=wholeData[$("input[type='radio']:checked").val()];
                //alert(chooseData.ch_disease);
                //$('#disease_span').text($(this).attr('id'));
                initCitys(Citys[chooseData.ch_province]);
            }else{
                initCitys(null);
            }
            console.log($(this).val());
            reData();
        });
        $('#city').change(function () {
              chooseData.ch_city=$(this).val();
            console.log($(this).val());
            reData();
        });
        //监听等级
        $("#level").change(function () {
            chooseData.ch_level=$(this).val();
            console.log($(this).val());
            reData();
        });
        //监听专科
        $("#features").change(function () {
            chooseData.ch_feature=$(this).val();
            console.log($(this).val());
            reData();
        });
        //监听左侧标签
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
