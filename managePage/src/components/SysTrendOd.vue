<template>
  <div class="tem">
    <div id="infoOD"></div>
  </div>
</template>

<script>
import { setTimeout } from "timers";
export default {
  name: "SysTrendOd",
  created() {
    setTimeout(() => {
      this.createEchart();
    }, 1500);
  },
  methods: {
    createEchart() {
      var echarts = this.$echarts;
      var option = {
        legend: {
          data: ["光密度比值"],
          top: "4%",
          textStyle: {
            color: "#fff"
          }
        },
        xAxis: {
          splitLine: {
            lineStyle: {
              type: "dashed",
              color: "gray"
            },
            show: true
          },
          axisLine: {
            lineStyle: {
              color: "#fff"
            }
          },
          type: "category",
          data: ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        },
        grid: {
          left: "2%",
          right: "2%",
          bottom: "4%",
          containLabel: true
        },
        tooltip: {
          trigger: "axis",
          axisPointer: {
            animation: false,
            lineStyle: {
              color: "#376df4",
              width: 1,
              opacity: 1
            }
          }
        },
        yAxis: {
          type: "value",
          splitLine: {
            lineStyle: {
              type: "dashed",
              color: "gray"
            },
            show: true
          },
          axisLine: {
            lineStyle: {
              color: "#fff"
            }
          }
        },
        series: [
          {
            data: [820, 670, 1007, 590, 1290, 920, 1320],
            type: "line",
            name: "光密度比值",
            smooth: true,
            itemStyle: {
              color: "#32CD32"
            },
            markPoint: {
              data: [
                { type: "max", name: "最大值" },
                { type: "min", name: "最小值" }
              ]
            }
          }
        ]
      };
      var dom = document.getElementById("infoOD");
      var myChart = echarts.init(dom);
      myChart.setOption(option);
      window.addEventListener("resize", function() {
        myChart.resize();
      });
    }
  }
};
</script>

<style scoped>
.tem {
  background: #000;
  height: 506px;
}
#infoOD {
  height: 100%;
}
</style>