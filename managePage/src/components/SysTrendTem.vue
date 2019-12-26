<template>
  <div class="tem">
    <div id="info"></div>
  </div>
</template>

<script>
export default {
  name: "SysTrendTem",
  props: ["times", "temp"],
  data() {
    return {
      yValue: this.temp,
      xValue: this.times
    };
  },
  created() {
    // this.initEchart();
    this.createEchart();
  },
  methods: {
    initEchart() {
      var count = 0;
      if (this.times.length <= 15) {
        count = 1;
      } else if (this.periodTime.length <= 35) {
        count = 3;
      } else if (this.periodTime.length < 60) {
        count = 5;
      } else if (this.periodTime.length < 300) {
        count = 23;
      } else if (this.periodTime.length < 600) {
        count = 100;
      } else if (this.periodTime.length < 2000) {
        count = 200;
      } else {
        count = 400;
      }
      var echarts = this.$echarts;
      var option = {
        legend: {
          data: ["反应温度"],
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
            },
            interval: count
          },
          type: "category",
          data: this.times
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
            data: this.temp,
            type: "line",
            smooth: true,
            name: "反应温度",
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
      var dom = document.getElementById("info");
      var myChart = echarts.init(dom);
      myChart.setOption(option);
      window.addEventListener("resize", function() {
        myChart.resize();
      });
    },
    createEchart() {
      var count = 0;
      if (this.times.length <= 15) {
        count = 1;
      } else if (this.periodTime.length <= 35) {
        count = 3;
      } else if (this.periodTime.length < 60) {
        count = 5;
      } else if (this.periodTime.length < 300) {
        count = 23;
      } else if (this.periodTime.length < 600) {
        count = 100;
      } else if (this.periodTime.length < 2000) {
        count = 200;
      } else {
        count = 400;
      }
      setInterval(() => {
        var echarts = this.$echarts;
        var option = {
          legend: {
            data: ["反应温度"],
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
              },
              interval: count
            },
            type: "category",
            data: this.times
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
              data: this.temp,
              type: "line",
              smooth: true,
              name: "反应温度",
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
        var dom = document.getElementById("info");
        var myChart = echarts.init(dom);
        myChart.setOption(option);
        window.addEventListener("resize", function() {
          myChart.resize();
        });
      }, 10000);
    }
  }
};
</script>

<style scoped>
.tem {
  background: #000;
  height: 506px;
}
#info {
  height: 100%;
}
</style>