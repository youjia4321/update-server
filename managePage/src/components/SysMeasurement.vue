<template>
  <div class="demo-split">
    <Split v-model="split2" mode="vertical">
      <div slot="top" class="demo-split-pane">
        <h5>
          <strong>测量配置</strong>
        </h5>
        <div class="setup">
          <div class="sub-set-up">
            测量&nbsp;&nbsp;
            <i-Switch size="large" @on-change="measureOn">
              <span slot="open">ON</span>
              <span slot="close">OFF</span>
            </i-Switch>
          </div>
          <div class="info">
            <p class="top">
              <Icon :type="measure" size="60" />&nbsp;&nbsp;&nbsp;&nbsp;
              间隔&nbsp;&nbsp;&nbsp;
              <Input v-model="times1" size="small" style="width: 50px" />&nbsp;&nbsp;小时测量一次
            </p>
            <p class="bottom">
              稀释&nbsp;&nbsp;
              <i-Switch size="large" @on-change="dilutionOn">
                <span slot="open">ON</span>
                <span slot="close">OFF</span>
              </i-Switch>&nbsp;&nbsp;&nbsp;&nbsp;
              <Icon :type="dilution" size="60" />&nbsp;&nbsp;&nbsp;&nbsp;
              稀释倍数&nbsp;&nbsp;&nbsp;
              <Input v-model="times2" size="small" style="width: 50px" />
            </p>
          </div>
        </div>
      </div>
      <div slot="bottom" class="demo-split-pane">
        <h5>
          <strong>预警设置</strong>
        </h5>
        <div class="setup">
          <div class="sub-set-up">
            预警&nbsp;&nbsp;
            <i-Switch size="large" @on-change="warningOn">
              <span slot="open">ON</span>
              <span slot="close">OFF</span>
            </i-Switch>
          </div>
          <div class="info">
            <p class="top">
              <Icon :type="warning" size="60" />&nbsp;&nbsp;&nbsp;&nbsp;
              预警上限值&nbsp;&nbsp;&nbsp;
              <Input v-model="top" size="small" style="width: 50px" />&nbsp;&nbsp;mg/L
            </p>
            <p class="top">
              <Icon :type="warning" size="60" />&nbsp;&nbsp;&nbsp;&nbsp;
              预警下限值&nbsp;&nbsp;&nbsp;
              <Input v-model="bottom" size="small" style="width: 50px" />&nbsp;&nbsp;mg/L
            </p>
          </div>
        </div>
      </div>
    </Split>
  </div>
</template>

<script>
export default {
  name: "SysMeasurement",
  data() {
    return {
      split2: 0.5,
      result: "None",
      active: 0,
      times1: "4",
      times2: "0",
      top: "0.5",
      bottom: "0",
      measure: "ios-alarm-outline",
      dilution: "ios-flask-outline",
      warning: "ios-notifications-outline"
    };
  },
  methods: {
    measureOn(bool) {
      if (bool) {
        this.measure = "ios-alarm";
      } else {
        this.measure = "ios-alarm-outline";
      }
    },
    dilutionOn(bool) {
      if (bool) {
        this.dilution = "ios-flask";
      } else {
        this.dilution = "ios-flask-outline";
      }
    },
    warningOn(bool) {
      if (bool) {
        this.warning = "ios-notifications";
      } else {
        this.warning = "ios-notifications-outline";
      }
    }
  }
};
</script>

<style scoped>
.demo-split {
  height: 506px;
  border: 1px solid #dcdee2;
}
.demo-split-pane {
  padding: 10px;
}
h5 {
  width: 20%;
  height: 240px;
  line-height: 240px;
  float: left;
  text-align: center;
}
.setup {
  width: 75%;
  height: 240px;
  float: right;
}
.table {
  margin-bottom: 0;
  height: 240px;
}
strong {
  font-size: 15px;
  color: #0f0a52;
}
.sub-set-up {
  font-size: 14px;
  line-height: 240px;
  float: left;
  width: 20%;
}
.top,
.bottom {
  height: 120px;
  line-height: 120px;
  font-size: 14px;
}
</style>