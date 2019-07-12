
var barViz=(function ($) {
    var _self = {},
        wholeData,
        myChart1,
        myChart2,
        option1,
        option2;

    function initView() {
        myChart1=echarts.init(document.getElementById('main-1'));
        myChart2=echarts.init(document.getElementById('main-2'));
                option1 = {
                    tooltip:{
                        padding: 10,
                        backgroundColor: '#222',
                        borderColor: '#777',
                        borderWidth: 1,
                        formatter: function (obj) {
                            var value = obj.value;
                            return '<div style="border-bottom: 1px solid rgba(255,255,255,.3); font-size: 18px;padding-bottom: 7px;margin-bottom: 7px">'
                                + obj.seriesName + '</div>'
                               + '指标：'+ value[0] + '<br>'
                               +'检查结果：' + value[1] + '<br>'
                               +'检查状态：' + value[2] + '<br>';
                        }
                    },
                    dataset: {source:wholeData.series1},
                    xAxis: {
                        max:1,
                        show:false,
                    },
                    grid:{
                        x:150
                    },
                    yAxis:{
                        type:'category',
                        axisTick: {show: false},
                        axisLine: {show: false},
                        axisLabel:{
                            textStyle:{
                                color: '#9b9b9b',
                                fontSize: 25,
                                fontWeight: 400,
                                lineHeight: 25
                            },
                        }
                    },
                    visualMap: {
                        orient: 'horizontal',
                        selectedMode:'multiple',
                        left: 'center',
                        dimension: 2,
                        categories:['偏低','正常','偏高'],
                        inRange: {
                            symbol:'circle',
                            color:['#4472C5','#EEE685','#fb7d7d']
                        },
                        textStyle:{
                            color: '#9b9b9b',
                            fontSize: 16.08,
                            fontWeight: 400,
                            lineHeight: 20
                        },
                        bottom:'5%'
                    },
                    series:
                        {
                            name:'类一指标',
                            type: 'bar',
                            barWidth:25,
                            itemStyle: {
                                emphasis: {
                                    barBorderRadius:[0,15,15,0]
                                },
                                normal: {
                                    barBorderRadius: [0,15,15,0]
                                }
                            }
                        }

                };
                option2={
                    tooltip:{
                        padding: 10,
                        backgroundColor: '#222',
                        borderColor: '#777',
                        borderWidth: 1,
                        formatter: function (obj) {
                            var value = obj.value;
                            return '<div style="border-bottom: 1px solid rgba(255,255,255,.3); font-size: 18px;padding-bottom: 7px;margin-bottom: 7px">'
                                + obj.seriesName + '</div>'
                                + '指标：'+ value[0] + '<br>'
                                +'检查结果：' + value[1] + '<br>'
                                +'检查状态：' + value[2] + '<br>';
                        }
                    },
                    dataset: {source:wholeData.series2
                        },
                    grid:{
                        x:150
                    },
                    xAxis:
                        {
                            show:false,
                        },
                    yAxis:
                        {
                            type:'category',
                            axisTick: {show: false},
                            axisLine: {show: false},
                            axisLabel: {
                                textStyle:{
                                    color: '#9b9b9b',
                                    fontSize: 25,
                                    fontWeight: 400,
                                    lineHeight: 25
                                }
                            }
                        },
                    visualMap:
                        {
                            orient: 'horizontal',
                            selectedMode:'multiple',
                            left: 'center',
                            dimension: 2,
                            categories:['正常','异常'],
                            bottom:'5%',
                            inRange: {
                                symbol:'circle',
                                color:['#4275EE','#FB7D7D']
                            },
                            textStyle:{
                                color: '#9b9b9b',
                                fontSize: 16.08,
                                fontWeight: 400,
                                lineHeight: 20
                            },
                        },
                    series:
                        {
                            name:'类二指标',
                            type:'bar',
                            barWidth:25,
                            itemStyle: {
                                emphasis: {
                                    barBorderRadius:[0,15,15,0]
                                },
                                normal: {
                                    barBorderRadius: [0,15,15,0]
                                }
                            }
                        }
                };
                myChart1.setOption(option1);
                myChart2.setOption(option2);
    }
    function loadData() {
        $.ajax({
            url: '/myechartsite/index_customer/userindi_data',
            type: 'GET',
            dataType: 'json',
            success: function (data) {
                wholeData = data;
                initView();
            }
        });
    }
    function initEvents() {
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
    barViz.init();
    //PointerEventsPolyfill.initialize({});
});
