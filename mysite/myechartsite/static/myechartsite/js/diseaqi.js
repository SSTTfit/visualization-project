
var scatterViz=(function ($) {
    var _self = {},
        time,
        disease,
        pollutions,
        wholeData,
        myChart,
        option,
        sourceData=[],
        chooseData={},
        //colors = ["334d5c","45b29e","efc94c","e27a3f","df4949","aeaeae","776355","57385c","4edaef","8db500"]
        radioTemplate = '<div class="radioItem"><input type="radio" name="Disease" class="radio"><label></label></div>',
        //  radioTemplate='<input type="radio" name="Disease" class="radio"><label class="control"></label><br>',
        buttonTemplate='<div class="buttonItem"><input type="button" class="btn-year normal"></div>',
        itemStyle = {
        normal: {
            opacity: 0.4,
            shadowBlur: 10,
            shadowOffsetX: 0,
            shadowOffsetY: 0,
            shadowColor: 'rgba(0, 0, 0, 0.5)'
        }
    };

    var sizeFunction = function (x) {
        var y = Math.sqrt(x / 5e8) + 0.1;
        return y * 600;
    };
    var schema = [
        {name: 'percent', index: 0, text: '发病率', unit: '%'},
        {name: 'PM2.5', index: 1, text: 'PM2.5', unit: ''},
        {name: 'PM10', index: 2, text: 'PM10', unit: ''},
        {name: 'NO2', index: 3, text: 'NO2', unit: ''},
        {name: 'SO2', index: 4, text: 'SO2', unit: ''},
        {name: 'O3', index: 5, text: 'O3', unit: ''},
        {name: 'CO', index: 6, text: 'CO', unit: ''}
    ];

    function  initControl() {
        //设置疾病单选框
        $.each(disease, function(index){
            var snippet = $(radioTemplate);
            if (index==0) {
                snippet.find('label').text(this).attr('for','item'+index).end()
                    .find('.radio').attr('value',this).attr('checked','checked').attr('id','item'+index).end()
                    .appendTo("#disease_choose");
                //console.log(this);
            }else
            {
                snippet.find('label').text(this).attr('for','item'+index).end()
                    .find('.radio').attr('value',this).attr('id','item'+index).end()
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
        $(".buttonItem").css({"margin-bottom":'11px'});
        rebtSkin();
        //$(".b").css({});
    }

    function initView() {
        myChart=echarts.init(document.getElementById('main'));
        option = {
            dataset:{
                source:sourceData
            },
            color: ['#BD61F9', '#5A8EF4', '#29CB97','#FFBC94', '#FFD839', '#FF8039' ],
            grid:{
                x:100,
                y:149,
                x2:80,
                y2:80
            },
            legend:
                {
                    width:300,
                    selectedMode: 'multiple',
                    orient:'horizontal',
                    top: 0,
                    itemGap:43,
                    itemWidth: 15,
                    top:40,
                    right:0,
                    data: pollutions,
                    formatter: function( name ) {
                        return '{a|' + name + '}';
                    },
                    textStyle:{
                        fontSize:18,
                        color:'#748aa1',
                        fontWeight:400,
                        lineHeight:23,
                        rich:{
                            a: {
                                width: 50
                            }
                        }
                    }
                },
            tooltip: {
                trigger: 'axis',
                axisPointer: {            // 坐标轴指示器，坐标轴触发有效
                    type: 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
                },
                formatter: function (params) { // 改鼠标悬浮提示值格式
                    var value = params[0].value;
                    var relVal =chooseData.ch_disease + "<br/>" + schema[0].text+ ' : ' + value[0]+ "<br/>"
                    +schema[1].text+' : '+value[1] + "<br/>"
                        +schema[2].text+' : '+value[2] + "<br/>"
                        +schema[3].text+' : '+value[3] + "<br/>"
                        +schema[4].text+' : '+value[4] + "<br/>"
                        +schema[5].text+' : '+value[5] + "<br/>"
                        +schema[6].text+' : '+value[6] + "<br/>";
                    return relVal;
                }
            },
            xAxis: {
                type: 'log',
                name: '空气\n指数',
                max: 1000,
                //  min: 300,
                nameGap: 20,
                nameLocation: 'end',
                nameTextStyle: {
                    fontSize:20,
                    color:'#9b9b9b',
                    fontWeight:400,
                    lineHeight:23,
                },
                splitLine: {
                    show: true,
                    lineStyle:{
                        type:'dashed'}
                },
                 axisLabel: {
                  fontSize:15,
                     color:'#9b9b9b'
                }
            },
            yAxis: {
                type: 'value',
                name: '发病率',
                max: 0.4,
                nameLocation:'end',
                nameGap:10,
                nameTextStyle: {
                    fontSize:20,
                    color:'#9b9b9b',
                    fontWeight:400,
                    lineHeight:23,
                },
                splitLine: {
                    show: true,
                    lineStyle:{
                        type:'dashed'}
                },
                axisLabel: {
                    fontSize:15,
                    color:'#9b9b9b'
                }
            },
            series: [
                {
                    name: pollutions[0],
                    type: 'scatter',
                    encode:{
                        y:0,
                        x:1
                    },
                    symbolSize:function(data) {
                        return sizeFunction(data
                        [1]);
                    },
                    itemStyle: itemStyle
                },
                {
                    name: pollutions[1],
                    type: 'scatter',
                    itemStyle: itemStyle,
                    symbolSize:function(data) {
                        return sizeFunction(data
                            [2]);
                    },
                    encode:{
                        y:0,
                        x:2
                    }
                },
                {
                    name: pollutions[2],
                    type: 'scatter',
                    itemStyle: itemStyle,
                    symbolSize:function(data) {
                        return sizeFunction(data
                            [3]);
                    },
                    encode:{
                        y:0,
                        x:3
                    }
                },
                {
                    name: pollutions[3],
                    type: 'scatter',
                    itemStyle: itemStyle,
                    symbolSize:function(data) {
                        return sizeFunction(data
                            [4]);
                    },
                    encode:{
                        y:0,
                        x:4
                    }
                },
                {
                    name: pollutions[4],
                    type: 'scatter',
                    itemStyle: itemStyle,
                    symbolSize:function(data) {
                        return sizeFunction(data
                            [5]);
                    },
                    encode:{
                        y:0,
                        x:5
                    }
                },
                {
                    name: pollutions[5],
                    type: 'scatter',
                    itemStyle: itemStyle,
                    symbolSize:function(data) {
                        return sizeFunction(data
                            [6]);
                    },
                    encode:{
                        y:0,
                        x:6
                    }
                }
            ],
        };
        myChart.setOption(option);
    }
    function loadData() {
        $.ajax({
            url: '/myechartsite/index_expert/diseaqi_data',
            type: 'GET',
            dataType: 'json',
            success: function (data) {
                wholeData = data.data;
                disease=data.disease;
                pollutions=data.pollution;
                time=data.timeline;
                chooseData.ch_disease=disease[0];
                chooseData.ch_year=time[0];
                chooseData.ch_data=wholeData[chooseData.ch_disease];
                sourceData.push(chooseData.ch_data[0]);
                //var dat=chooseData.ch_data;
                console.log(chooseData.ch_data[0]);
                initControl();
                initView();
            }
        });
    }

    function reData() {
        chooseData.ch_data=wholeData[chooseData.ch_disease];
        var index=Math.max.apply(null,time)-chooseData.ch_year;
        sourceData.length=0;
        sourceData.push(chooseData.ch_data[index]);
        console.log(sourceData);
        myChart.setOption({
            dataset:{
                source:sourceData
            }
        });
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
            $('#disease_span').text($(this).val());
            console.log(this);
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
            //  if ($(this).hasClass("normal"))
            //  {
            //      $(this).removeClass("normal").addClass("selected").siblings().css("background",'yellow')
            //.removeClass("selected").addClass("normal");
            //      console.log($(this).siblings());
            //  }else
            //  {
            //      $(this).siblings().removeClass("selected").addClass("normal");
            //   }
            rebtSkin();

            //  chooseData.ch_year=chooseDom.val();
            //console.log(chooseData.ch_year);
        });
        //监听左侧按钮
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
    scatterViz.init();
    //PointerEventsPolyfill.initialize({});
});
