var numYear = 2018;
var diseaseName;
var diseaseValue = 'sy';
var data_data;
var dataJson;
var a='';
$(document).ready(function(){
    $.ajaxSetup({
        async : false
    });
    // location.reload(false);
    $.ajax({
        url: '/myechartsite/index_expert/diseage_data',
        type: 'GET',
        dataType: 'json',
        success: function (data) {
            data_data=data;
            // alert('success');
        },
        error: function () {
            alert('未能加载数据')
        }
    })
    $(".btn-year").removeClass("rbtnact1");
    $('#2018').addClass("rbtnact1");
    dataJson=data_data[numYear][diseaseValue];
    loadData();
});

//radio事件
function changeRadio(disease)
{
    disease.style.backgroundImage = 'url(../img/Assets.png)';
    diseaseName =$('input:radio[name="disease"]:checked').next("label").text();
    diseaseValue =$('input:radio[name="disease"]:checked').val();
    a=diseaseName;
    changeDiseaseLabel(diseaseName);
    var radio = document.getElementsByName("disease");
    loadData();
}

function btnclick(numid) {
    $(".btn-year").removeClass("rbtnact1");
    $(numid).addClass("rbtnact1");
    numYear=numid.id;
    changeYearLabel(numYear);
    loadData()
}
function changeYearLabel(numYear) {
    document.getElementById('year1').innerHTML = numYear+'年';
    document.getElementById('year2').innerHTML = numYear;
}
function changeDiseaseLabel(disease) {
    document.getElementById('disease1').innerHTML = disease;
    document.getElementById('disease2').innerHTML = disease;
}
function changeDisease(disease) {
    disease.style.backgroundImage = 'url(../img/Assets1.png)';
}
function loadData() {
    dataJson=data_data[numYear][diseaseValue];
    var myChart2 = echarts.init(document.getElementById('main4'));
    myChart2.setOption({

        series: [{
            name:diseaseName,
            // 根据名字对应到相应的系列
            data: dataJson
        }]
    });
}

//图表
   //疾病名称，例 溶血性黄疸
//细化疾病与年龄的关系展示
b='溶血性黄疸'
option4 = {
    backgroundColor: "#f5f6fa",
    // title: {
    //     text: a+'在不同年龄段中的分布',
    //     //subtext: '纯属虚构',
    //     // subtext:a+'在不同年龄段中的分布',
    //     x: 'left',
    //     top: '10',
    //     left:'10',
    //     textStyle: {
    //         color: "#9b9b9b",
    //     }
    // },
    //显示series中信息，提示框组件
    tooltip: {
        trigger: 'item',
        formatter: "{a} <br/>{b} : {c} ({d}%)"  //提示框显示格式

    },
    grid:{
        // top:'20%',
    },
    color:['#2d85f1','#4a89f1','#1965e8','#165bd2','#124cb1','#0e3e8e','#0e18f1','#2506f1'],
    series: [{
        name:'急慢性肾炎',   //疾病名称，例 溶血性黄疸
        type: 'pie', //图表类型，柱状图：bar
        //饼图：pie  (南丁格尔图在series中加上roseType:’angle’)移开后不显示原来信息
        radius: '55%', //半径
        center: ['50%', '50%'],
        label: {
            formatter: "{b}岁 : {d}%"
        },
        data: dataJson,
        itemStyle: { //itemStyle有正常显示：normal，有鼠标hover的高亮显示：emphasis
            emphasis: { //normal显示阴影,与shadow有关的都是阴影的设置
                shadowBlur: 10, //阴影大小
                shadowOffsetX: 0, //阴影水平方向上的偏移
                shadowColor: 'rgba(0, 0, 0, 0.5)' //阴影颜色
            }
        }
    }]
};
