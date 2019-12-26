<template>
  <div class="demo-split">
    <Split v-model="split2" mode="vertical">
      <div slot="top" class="demo-split-pane">
        <h5>
          <strong>当前测量值：</strong>
        </h5>
        <div class="result">
          <div class="sub">
            <strong style="font-size: 20px">{{ result }}</strong>&nbsp;&nbsp;&nbsp; mg/L
          </div>
        </div>
      </div>
      <div slot="bottom" class="demo-split-pane">
        <h5>
          <strong>测量进度：</strong>
        </h5>
        <div class="process">
          <el-steps :active="active" finish-status="success" process-status="proccess" align-center>
            <el-step title="润洗"></el-step>
            <el-step title="加酸"></el-step>
            <el-step title="稀释"></el-step>
            <el-step title="加热"></el-step>
            <el-step title="UV"></el-step>
            <el-step title="显色"></el-step>
            <el-step title="测量"></el-step>
            <el-step title="清洗"></el-step>
          </el-steps>
        </div>
        <el-progress
          type="circle"
          :width="90"
          :percentage="percentage"
          :style="obj"
          :color="colors"
        ></el-progress>
        <div class="btns">
          <el-button style="margin-top: 12px;" @click="next">单次测量</el-button>
          <el-button style="margin-top: 12px;" @click="continuous1">连续测量</el-button>
          <el-button style="margin-top: 12px;" @click="stop">停止测量</el-button>
        </div>
      </div>
    </Split>
  </div>
</template>

<script>
import { setInterval, clearInterval } from "timers";
export default {
  name: "SysCarlibration",
  data() {
    return {
      split2: 0.4,
      result: "None",
      active: 0,
      myBar: "",
      percentage: 0,
      colors: [
        { color: "#f56c6c", percentage: 20 },
        { color: "#e6a23c", percentage: 40 },
        { color: "#5cb87a", percentage: 60 },
        { color: "#1989fa", percentage: 80 },
        { color: "#6f7ad3", percentage: 100 }
      ],
      obj: {
        marginTop: "30px",
        marginLeft: "50px"
      }
    };
  },
  methods: {
    next() {
      this.percentage = 0;
      clearInterval(this.myBar);
      if (this.active++ > 7) this.active = 0;
    },
    continuous1() {
      this.percentage = 0;
      this.active = 0;
      this.myBar = setInterval(() => {
        this.percentage += Math.floor(Math.random() * 20) + 1;
        this.active++;
        if (this.active > 7) {
          this.percentage = 100;
          this.active = 0;
          this.result = (Math.random() * (1 - 5) + 5).toFixed(2);
          clearInterval(this.myBar);
        }
      }, 2000);
    },
    startOne() {
      var socket = new WebSocket("ws://127.0.0.1:8080/one_reagent?equipId=1");
      socket.onopen = function() {
        //若是连接成功，onopen函数会执行
        socket.send("send msg 1");
      };
      socket.onmessage = function(ev) {
        // 前端数据接收
        // eslint-disable-next-line
        console.log(ev.data);
        if (ev.data === "allowed") {
          this.continuous1();
        } else {
          this.stop();
        }
      };
    },
    stop() {
      clearInterval(this.myBar);
      this.active = 0;
      this.percentage = 0;
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
.sub {
  width: 170px;
  margin: 0 auto;
  line-height: 170px;
  font-size: 16px;
}
.process {
  padding-top: 70px;
}
.btns {
  width: 420px;
  margin-top: 40px;
  float: right;
}
</style>