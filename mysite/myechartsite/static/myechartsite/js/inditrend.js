var zhexianData=[[],[],[],[],[],[],[],[],[],[],[]];
var Jsonzhexian;//获取折线总数据
window.onload=function(){


    loadData();

}
function loadData() {
  $.get('/myechartsite/index_customer/inditrend_data', function (data) {
      Jsonzhexian = data;
  });
    var myChart = echarts.init(document.getElementById('zhexianJson'));
    myChart.setOption({
        series:[
            {data:Jsonzhexian['tt'].value},
            ]
    });
    a = document.getElementById('tt');
    choosezhibiao(a,'rbtnact1',0,'tt','酮体')
}
$.get('/myechartsite/index_customer/inditrend_data', function (data) {
    Jsonzhexian = data;
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
    var myChart = echarts.init(document.getElementById('zhexianJson'));
    myChart.setOption(optionZhexian,true);
});
//折线图总数据
var optionZhexian = {
    // title: {
    //     text: '检查项目',
    // },

    tooltip: {
        trigger: 'axis'
    },
    legend: {
        // data:['PH','肌酐','尿比重','尿胆原','微量蛋白','sdfgg','dfg'],
        // data: data.name,
        // top:'1%',
        // left:'35%'
    },
    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },
    toolbox: {
        feature: {
            saveAsImage: {}
        }
    },
    xAxis: {
        gridIndex: 0,
        splitLine:{show: true},//去除网格线
        // splitArea : {show : true},//保留网格区域
        axisLabel: {
            show: true,
            textStyle: {
                color: '9B9B9B',
                fontSize:15,
            }
        },
        axisLine: {
            lineStyle:{
                color:'#D8D8D8',//x轴的颜色
                width:8,//轴线的宽度
                }
            },

        type: 'category',
        boundaryGap: false,
        data: ['2013.06', '2013.12', '2014.06', '2014.12', '2015.06', '2015.12','2016.06', '2016.12', '2017.06', '2017.12', '2018.06', '2018.12']
    },
    yAxis: {
        axisLabel: {
            show: true,
            textStyle: {
                color: '9B9B9B',
                fontSize:15,
            }
        },
        splitLine:{show: true},//去除网格线
        // splitArea : {show : true},//保留网格区域
        axisLine: {
            lineStyle:{
                color:'#D8D8D8',//x轴的颜色
                width:8,//轴线的宽度
            }
        },
        type: 'value'
    },
    series: [
        {
            symbolSize: 0, //拐点大小15
            itemStyle: {
                normal: {
                    color:"#b558f6",//折线点的颜色
                    lineStyle: {
                        width: 8, //折线宽度
                        color:"#b558f6",
                    }
                }
            },
            // name: '胴体',
            type: 'line',
            data: [],
        },
        {
            symbolSize: 0, //拐点大小
            itemStyle: {
                normal: {
                  color:'#4578ef',
                    lineStyle: {
                        width: 8, //折线宽度
                        color:'#4578ef',
                    }
                }
            },
            // name: '亚硝酸盐',
            type: 'line',
            data: [],
        },
        {
            symbolSize: 0, //拐点大小
            itemStyle: {
                normal: {
                    color:'#29cb97',
                    lineStyle: {
                        width: 8, //折线宽度
                        color:'#29cb97',
                    }
                }
            },
            // name: '葡萄糖',
            type: 'line',
            data: [],
        },
        {
            symbolSize: 0, //拐点大小
            itemStyle: {
                normal: {
                  color:'#ffc7c7',
                    lineStyle: {
                        width: 8, //折线宽度
                        color:'#ffc7c7',
                    }
                }
            },
            // name: '胆红素',
            type: 'line',
            data: [],
        },
        {
            symbolSize: 0, //拐点大小
            itemStyle: {
                normal: {
                  color:'#ffd839',
                    lineStyle: {
                        width: 8, //折线宽度
                        color:'#ffd839',
                    }
                }
            },
            // name: '钙',
            type: 'line',
            data: [],
        },
        {
            symbolSize: 0, //拐点大小
            itemStyle: {
                normal: {
                  color:'#e35f17',
                    lineStyle: {
                        width: 8, //折线宽度
                        color:'#e35f17',
                    }
                }
            },
            // name: '折线1',
            type: 'line',
            data: [],
        },
        {
            symbolSize: 0, //拐点大小
            itemStyle: {
                normal: {
                    color:'#2a1788',
                    lineStyle: {
                        width: 8, //折线宽度
                        color:'#2a1788',
                    }
                }
            },
            // name: '折线2',
            type: 'line',
            data: [],
        },
        {
            symbolSize: 0, //拐点大小
            itemStyle: {
                normal: {
                  color:'#aed405',
                    lineStyle: {
                        width: 8, //折线宽度
                        color:'#aed405',
                    }
                }
            },
            // name: '折线3',
            type: 'line',
            data: [],
        }
    ]
};
var zhexianNum=[0,0,0,0,0,0,0,0]
function choosezhibiao(a,css,i,leibie,disen){
    $(a).toggleClass("rbtnnorm");
    $(a).toggleClass(css);
    // optionZhexian.series[0].data[i].name = Jsonzhexian[leibie].name;
    // optionZhexian.series[0].data[i].value = Jsonzhexian[leibie].value;
    if(zhexianNum[i]==0){
        var myChart = echarts.init(document.getElementById('zhexianJson'));
        zhexianData[i]=Jsonzhexian[leibie]['value'];
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
        var myChart = echarts.init(document.getElementById('zhexianJson'));
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

// function choosezhibiao(a,css,i,leibie,disen){
//     $(a).toggleClass("rbtnnorm");
//     $(a).toggleClass(css);
//     // optionZhexian.series[0].data[i].name = Jsonzhexian[leibie].name;
//     // optionZhexian.series[0].data[i].value = Jsonzhexian[leibie].value;
//     if(zhexianNum[i]==0){
//         var myChart = echarts.init(document.getElementById('zhexianJson'));
//         myChart.setOption({
//
//             series: [{
//                 // 根据名字对应到相应的系列
//                 data: Jsonzhexian[leibie].value
//             }]
//         });
//         zhexianNum[i]=!zhexianNum[i];
//     }
//     else {
//         var myChart = echarts.init(document.getElementById('zhexianJson'));
//         myChart.setOption({
//
//             series: [{
//                 // 根据名字对应到相应的系列
//                 data: []
//             }]
//         });
//         zhexianNum[i]=!zhexianNum[i];
//     }
//     // myChart.setOption(optionZhexian,true);
//
// };
