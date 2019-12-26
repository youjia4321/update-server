<template>
  <div class="main">
    <div class="container">
      <div class="content">
        <Button size="small" type="primary" ghost @click="back()">
          <Icon type="ios-arrow-back" />选择设备
        </Button>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        <Tag type="dot" color="primary">
          <i style="font-size: 14px; font-weight: 600;">微试剂设备 {{ equipId }}</i>
        </Tag>

        <br />
        <br />
        <div class="main-window">
          <div class="sub-title">
            <div class="img" style="float: left">
              <img src="../../assets/logo/logo-o.png" />
            </div>
            <div class="text">
              <span>微试剂总磷在线检测仪</span>
            </div>
          </div>
          <el-tabs tab-position="left" style="height: 560px; width: 100%;">
            <el-tab-pane>
              <span slot="label">
                <i class="el-icon-loading"></i> 运行状态
              </span>
              <Tabs class="nav" name="state">
                <TabPane label="TP 状态" icon="ios-switch">
                  <SysState></SysState>
                </TabPane>
              </Tabs>
            </el-tab-pane>
            <el-tab-pane>
              <span slot="label">
                <i class="el-icon-s-data"></i> 参数趋势
              </span>
              <Tabs class="nav" name="trend">
                <TabPane label="温度趋势" icon="ios-pulse">
                  <SysTrendTem :times="tempX" :temp="tempY"></SysTrendTem>
                </TabPane>
                <TabPane label="OD 趋势" icon="md-pulse">
                  <SysTrendOd></SysTrendOd>
                </TabPane>
              </Tabs>
            </el-tab-pane>
            <el-tab-pane>
              <span slot="label">
                <i class="el-icon-aim"></i> 仪器校准
              </span>
              <Tabs class="nav" name="calibration">
                <TabPane label="校准操作" icon="md-locate">
                  <SysCalibrationOperate></SysCalibrationOperate>
                </TabPane>
                <TabPane label="校准历史" icon="md-document">
                  <SysCalibrationHistory></SysCalibrationHistory>
                </TabPane>
              </Tabs>
            </el-tab-pane>
            <el-tab-pane>
              <span slot="label">
                <i class="el-icon-thumb"></i> 仪器维护
              </span>
              <Tabs class="nav" name="maintenance">
                <TabPane label="TP 维护" icon="ios-construct">
                  <SysProtect></SysProtect>
                </TabPane>
              </Tabs>
            </el-tab-pane>
            <el-tab-pane>
              <span slot="label">
                <i class="el-icon-document"></i> 历史数据
              </span>
              <Tabs class="nav" name="history">
                <TabPane label="TP 历史数据" icon="md-document">
                  <SysTpHistory></SysTpHistory>
                </TabPane>
              </Tabs>
            </el-tab-pane>
            <el-tab-pane>
              <span slot="label">
                <i class="el-icon-odometer"></i> 测量配置
              </span>
              <Tabs class="nav" name="measurement-set-up">
                <TabPane label="TP 测量配置" icon="md-color-fill">
                  <SysMeasurement></SysMeasurement>
                </TabPane>
              </Tabs>
            </el-tab-pane>
            <el-tab-pane>
              <span slot="label">
                <i class="el-icon-s-platform"></i> 系统设置
              </span>
              <Tabs class="nav" name="system-set-up">
                <TabPane label="TP 系统设置" icon="md-laptop">
                  <SysState></SysState>
                </TabPane>
              </Tabs>
            </el-tab-pane>
          </el-tabs>
          <div class="sub-footer">
            <div class="footer-text">
              <span>{{ nowTime }}</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import SysCalibrationHistory from "@/components/SysCalibrationHistory";
import SysCalibrationOperate from "@/components/SysCalibrationOperate";
import SysState from "@/components/SysState";
import SysTrendTem from "@/components/SysTrendTem";
import SysTrendOd from "@/components/SysTrendOd";
import SysProtect from "@/components/SysProtect";
import SysTpHistory from "@/components/SysTpHistory";
import SysMeasurement from "@/components/SysMeasurement";

export default {
  name: "SysReagentDetail",
  data() {
    return {
      nowTime: "",
      equipId: "",
      tempX: [],
      tempY: []
    };
  },
  created() {
    this.nowTimes();
    this.equipId = this.$route.query.equipId;
    this.getTempData();
  },
  components: {
    SysCalibrationHistory,
    SysCalibrationOperate,
    SysState,
    SysTrendTem,
    SysTrendOd,
    SysProtect,
    SysTpHistory,
    SysMeasurement
  },
  methods: {
    getTempData() {
      setInterval(() => {
        this.$http.responseTemp().then(resp => {
          if (resp.data.code === "200") {
            this.tempX = resp.data.times;
            this.tempY = resp.data.temp;
          } else {
            this.$Message.error("温度读取失败...");
          }
        });
      }, 15000);
    },
    timeFormate(timeStamp) {
      let year = new Date(timeStamp).getFullYear();
      let month =
        new Date(timeStamp).getMonth() + 1 < 10
          ? "0" + (new Date(timeStamp).getMonth() + 1)
          : new Date(timeStamp).getMonth() + 1;
      let date =
        new Date(timeStamp).getDate() < 10
          ? "0" + new Date(timeStamp).getDate()
          : new Date(timeStamp).getDate();
      let hh =
        new Date(timeStamp).getHours() < 10
          ? "0" + new Date(timeStamp).getHours()
          : new Date(timeStamp).getHours();
      let mm =
        new Date(timeStamp).getMinutes() < 10
          ? "0" + new Date(timeStamp).getMinutes()
          : new Date(timeStamp).getMinutes();
      let ss =
        new Date(timeStamp).getSeconds() < 10
          ? "0" + new Date(timeStamp).getSeconds()
          : new Date(timeStamp).getSeconds();
      this.nowTime =
        year + "/" + month + "/" + date + " " + hh + ":" + mm + ":" + ss;
    },
    nowTimes() {
      this.timeFormate(new Date());
      setInterval(this.nowTimes, 1000);
      this.clear();
    },
    clear() {
      clearInterval(this.nowTimes);
      this.nowTimes = null;
    },
    back() {
      this.$router.go(-1); //返回上一层
    }
  }
};
</script>

<style scoped>
.head {
  text-align: center;
  font-size: 15px;
}
.main-window {
  box-shadow: 8px 8px 8px #888888;
}
.sub-title,
.sub-footer {
  width: 100%;
  height: 60px;
  background: #e6e5e4;
  border-left: 1px solid #d8d8d8;
}
.sub-title {
  border-top: 1px solid #d8d8d8;
}
.sub-footer {
  height: 50px;
}
.footer-text {
  float: right;
  font-size: 14px;
  line-height: 50px;
  margin-right: 10%;
}
img {
  margin-top: 15px;
  margin-left: 20px;
  width: 75%;
}
.text {
  float: right;
  line-height: 60px;
  font-size: 18px;
  margin-right: 32%;
  letter-spacing: 1px;
}
.nav {
  height: 559px;
  border: 1px solid #d8d4d4;
  margin: 0px 10px 0px 0px;
}
@media screen and (max-width: 1000px) {
  .text {
    margin-right: 8%;
  }
}
</style>