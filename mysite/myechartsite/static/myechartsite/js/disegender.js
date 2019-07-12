
var barViz=(function ($) {
    var _self = {},
        time,
        disease,
        age,
        wholeData,
        myChart,
        option,
        chooseData={},
        radioTemplate = '<div class="radioItem"><input type="radio" name="Disease" class="radio"><label></label></div>',
      //  radioTemplate='<input type="radio" name="Disease" class="radio"><label class="control"></label><br>',
        buttonTemplate='<div class="buttonItem"><input type="button" class="btn-year normal"></div>';
        //radioCss={background:'#e5e9f2',width:'100%'};

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

    function formatNumber(num) {
        for(var i=0;i<num.length;i++) {
            num[i] = -Math.abs(num[i]);
        }
        return num;
    }
    function initView() {
        myChart=echarts.init(document.getElementById('main'));
        option = {
            title: {
            },
            tooltip: {
                trigger: 'axis',
                axisPointer: {            // 坐标轴指示器，坐标轴触发有效
                    type: 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
                },
                formatter: function (params) { // 改鼠标悬浮提示值格式
                    var relVal = params[0].name + "<br/>";
                    relVal += params[0].seriesName + ' : ' + (-params[0].value) + "<br/>";
                    relVal += params[1].seriesName + ' : ' + params[1].value + "<br/>";
                    return relVal;
                }
            },

            legend: {
                data: [
                    {name:'男',
                        textStyle:{
                            color:'#67A2CD'
                        }
                    },{ name:'女',
                        textStyle:{
                            color:'#FFA7A6'
                        }}],
                icon:'none',
                itemGap:250,
                right:'30%',
                top: 4,
               // left: '32%',
                textStyle:{
                    fontSize:30,
                    fontWeight:400,
                    lineHeight:38
                }
            },

            grid: {
                top: 40,
                bottom: 50
            },
            xAxis: {
                type: 'value',
                axisLabel: {
                    formatter: function (value) {
                        return Math.abs(value) + '%'   //负数取绝对值变正数
                    }
                },
                axisLine: {show: false},
                splitLine: {show:false},
            },
            yAxis: {
                type: 'category',
                axisLine: {show: false},
                //axisLabel: {show: false},
                axisTick: {show: false},
                splitLine: {show: false},
                data: age,
                axisLabel: {
                    formatter:'{value}岁'
                }
            },
            series:
                [
                    {
                        name: '男', type: 'bar', stack:'百分比',data: formatNumber(chooseData.ch_data[0]),
                        barWidth:35,
                        itemStyle: {
                            emphasis: {
                                barBorderRadius:[15,0,0,15]
                            },
                            normal: {
                                barBorderRadius: [15,0,0,15],
                                color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [{offset: 0, color: '#4072EE'}, {offset: 1, color: '#74ABF8'}]
                                )
                            }}
                    },
                    {
                        name: '女', type: 'bar',stack:'百分比',data: chooseData.ch_data[1],
                        barWidth:35,
                        itemStyle: {
                            emphasis: {
                                barBorderRadius:[0,15,15,0]
                            },
                            normal: {
                                barBorderRadius: [0,15,15,0],
                                color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [{offset: 0, color: '#FFCCCC'}, {offset: 1, color: '#FB7A7A'}]
                                )
                            }}
                    }]
        };
        myChart.setOption(option);
    }
    function loadData() {
        $.ajax({
            url: '/myechartsite/index_expert/disegenderage_data',
            type: 'GET',
            dataType: 'json',
            success: function (data) {
                wholeData = data.data;
                disease=data.disease;
                age=data.age;
                time=data.time;
                chooseData.ch_disease=disease[0];
                chooseData.ch_year=time[0];
                chooseData.ch_data=wholeData[chooseData.ch_disease][chooseData.ch_year];
                //var dat=chooseData.ch_data;
                console.log(chooseData.ch_data[0]);
                initControl();
                initView();
            }
        });
    }

    function reData() {
        chooseData.ch_data=wholeData[chooseData.ch_disease][chooseData.ch_year];
        console.log(chooseData.ch_data)
        myChart.setOption(
            {
                series:
                    [
                        {
                            data: formatNumber(chooseData.ch_data[0])
                        },
                        {
                            data: chooseData.ch_data[1]
                        }]
            }
        )
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
            console.log(chooseData.ch_disease);
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
        /*监听左侧选择按钮*/
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
