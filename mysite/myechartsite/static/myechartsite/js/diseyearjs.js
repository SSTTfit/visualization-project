var JsonDieYear;
window.onload=function(){


    var zhexianNum=[0,0,0,0,0,0,0,0];
    var zhexianData=[[],[],[],[],[],[],[],[],[],[],[]];  //折线图总数据
    var btnleibie;

    loadData();

}
function loadData() {
  $.get('/myechartsite/index_expert/diseyear_data', function (data) {
      JsonDieYear = data;
      a = document.getElementById('rxxhd');
      chooseDieYearzhibiao(a,'rbtnact1',0,'rxxhd','溶血性黄疸');
  });
    var myChart = echarts.init(document.getElementById('jibingyunianfen'));
    myChart.setOption({
        series:[
            {data:JsonDieYear['rxxhd'].value},
            ]
    })
}
$.get('/myechartsite/index_expert/diseyear_data', function (data) {
    JsonDieYear = data;
    niaobizhong1=[];
    function niaobizhongchange()
    {
        for (var i = 0; i < data.name.length; i++) {
            for (var j=0;j<data.value[i].length;j++){
                niaobizhong1.push(data.value[i][j]/1.1)
            }
            alert(niaobizhong1);
            return niaobizhong1;
        }
    }
    var myChart = echarts.init(document.getElementById('jibingyunianfen'));
    myChart.setOption(optionJibingyunianfen,true);
});
var XAxis=[2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019];
optionJibingyunianfen = {
    title: {
        text: '发病率%'
    },
    tooltip : {
        trigger: 'axis',
        axisPointer: {
            type: 'cross',
            label: {
                backgroundColor: '#6a7985'
            }
        }
    },
    legend: {
        // data:['邮件营销','联盟广告','视频广告','直接访问','搜索引擎']
    },
    toolbox: {
        feature: {
            saveAsImage: {}
        }
    },
    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },
    xAxis : [
        {
            type : 'category',
            boundaryGap : false,
            // data : ['2013','2014','2015','2016','2017','2018','2019']
            data : XAxis
        }
    ],
    yAxis : [
        {
            type : 'value',
            axisLabel: {
                show: true,
                textStyle: {
                    color: '#9B9B9B',
                    fontSize:15,
                }
            },
        }
    ],
    series : [
        {
            // name:'邮件营销',
            symbolSize: 5, //拐点大小15
            itemStyle: {
                normal: {
                    color: "#b558f6",//折线点的颜色
                    lineStyle: {
                        width: 3, //折线宽度
                        color:"#c7c7c7",
                    }
                }
            },
            type:'line',
            stack: '总量',
            areaStyle: {},
            data:[]
        },
        {
            // name:'联盟广告',
            symbolSize: 5, //拐点大小15
            itemStyle: {
                normal: {
                    color: "#4578ef",//折线点的颜色
                    lineStyle: {
                        width: 3, //折线宽度
                        color:"#c7c7c7",
                    }
                }
            },
            type:'line',
            stack: '总量',
            areaStyle: {},
            data:[]
        },
        {
            // name:'邮件营销',
            symbolSize: 5, //拐点大小15
            itemStyle: {
                normal: {
                    color: "#29cb97",//折线点的颜色
                    lineStyle: {
                        width: 3, //折线宽度
                        color:"#c7c7c7",
                    }
                }
            },
            type:'line',
            stack: '总量',
            areaStyle: {},
            data:[]
        },
        {
            // name:'联盟广告',
            symbolSize: 5, //拐点大小15
            itemStyle: {
                normal: {
                    color: "#ffc7c7",//折线点的颜色
                    lineStyle: {
                        width: 3, //折线宽度
                        color:"#c7c7c7",
                    }
                }
            },
            type:'line',
            stack: '总量',
            areaStyle: {},
            data:[]
        },
        {
            // name:'视频广告',
            symbolSize: 5, //拐点大小15
            itemStyle: {
                normal: {
                    color: "#ffd839",//折线点的颜色
                    lineStyle: {
                        width: 3, //折线宽度
                        color:"#c7c7c7",
                    }
                }
            },
            type:'line',
            stack: '总量',
            areaStyle: {},
            data:[]
        },
        {
            // name:'直接访问',
            symbolSize: 5, //拐点大小15
            itemStyle: {
                normal: {
                    color: "#e35f17",//折线点的颜色
                    lineStyle: {
                        width: 3, //折线宽度
                        color:"#c7c7c7",
                    }
                }
            },
            type:'line',
            stack: '总量',
            areaStyle: {normal: {}},
            data:[]
        },
        {
            // name:'直接访问',
            symbolSize: 5, //拐点大小15
            itemStyle: {
                normal: {
                    color: "#2a1788",//折线点的颜色
                    lineStyle: {
                        width: 3, //折线宽度
                        color:"#c7c7c7",
                    }
                }
            },
            type:'line',
            stack: '总量',
            areaStyle: {normal: {}},
            data:[]
        },
        {
            // name:'搜索引擎',
            symbolSize: 5, //拐点大小15
            itemStyle: {
                normal: {
                    color: "#aed405",//折线点的颜色
                    lineStyle: {
                        width: 3, //折线宽度
                        color:"#e67b05",
                    }
                }
            },
            type:'line',
            stack: '总量',
            label: {
                normal: {
                    show: true,
                    position: 'top'
                }
            },
            areaStyle: {normal: {}},
            data:[]
        }
    ]
};


var zhexianNum=[0,0,0,0,0,0,0,0];
var zhexianData=[[],[],[],[],[],[],[],[],[],[],[]];  //折线图总数据
var btnleibie;
//指标
function chooseDieYearzhibiao(a,css,i,leibie,disen){
    $(a).toggleClass("rbtnnorm");
    $(a).toggleClass(css);
    btnleibie = leibie;
    // optionZhexian.series[0].data[i].name = Jsonzhexian[leibie].name;
    // optionZhexian.series[0].data[i].value = Jsonzhexian[leibie].value;
    if(zhexianNum[i]==0){
        var myChart = echarts.init(document.getElementById('jibingyunianfen'));
        zhexianData[i]=JsonDieYear[leibie]['value'];
        myChart.setOption({
            series:[
                {data:zhexianData[0]},
                {data:zhexianData[1]},
                {data:zhexianData[2]},
                {data:zhexianData[3]},
                {data:zhexianData[4]},
                {data:zhexianData[5]},
                {data:zhexianData[6]},
                {data:zhexianData[7]}]
        })
        // myChart.setOption(optionZhexian,true);
        zhexianNum[i]=!zhexianNum[i];
    }
    else {
        var myChart = echarts.init(document.getElementById('jibingyunianfen'));
        zhexianData[i]=[];
        myChart.setOption({
            series:[
                {data:zhexianData[0]},
                {data:zhexianData[1]},
                {data:zhexianData[2]},
                {data:zhexianData[3]},
                {data:zhexianData[4]},
                {data:zhexianData[5]},
                {data:zhexianData[6]},
                {data:zhexianData[7]}]
        })
        zhexianNum[i]=!zhexianNum[i];
    }
    // myChart.setOption(optionZhexian,true);

};

// $(document).ready(function(){
//     $.getJSON('/myechartsite/index_expert/disewheather_data',function(ret){
//         data = ret
//         p[0]=!p[0];
//         option.series[0].data[0].value = ret[year].nephritis;
//         $("#sy").removeClass("rbtnnorm");
//         $("#sy").toggleClass("rbtnact1");
//         $("#y2019").addClass("rbtnact");
//         myChart.setOption(option,true);
//     })
// });
