<template>
  <table class="table table-bordered table-striped">
    <thead>
      <tr>
        <th style="width: 162px">稀释配置</th>
        <th style="width: 220px">校准方式选择</th>
        <th style="width: 220px">校准液浓度配置</th>
        <th style="width: 100px">∆ O.D</th>
        <th style="width: 100px">(RSD)%</th>
        <th style="width: 100px">校准进度</th>
        <th style="width: 100px">校准操作</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td rowspan="3">
          <div class="dilution">
            <Icon type="ios-flask-outline" size="60" />
            <p>
              稀释&nbsp;
              <Input v-model="multiple" size="small" style="width: 50px" />&nbsp;倍
            </p>
          </div>
        </td>
        <td rowspan="3">
          <div class="choose" v-if="method !== ''">
            选择方式：
            <strong style="color: green">{{ method }}</strong>
          </div>
          <div class="choose" v-else>
            选择方式：
            <strong style="color: red">未选择</strong>
          </div>
          <div class="auto" @click="method = '自动校准'">
            <Button style="height: 110px">
              <Icon type="ios-speedometer-outline" size="80" />
              <br />
              <p>自动校准</p>
            </Button>
          </div>

          <div class="hand" @click="method = '手动校准'">
            <Button style="height: 110px">
              <Icon type="ios-construct-outline" size="80" />
              <br />
              <p>手动校准</p>
            </Button>
          </div>
        </td>
        <td rowspan="3">
          <div class="set-up" id="set-up-1">
            <Icon type="ios-color-fill" size="80" />
            <p> 
              <i>标液1</i>&nbsp;&nbsp;&nbsp;&nbsp;
              <Input v-model="water1" size="small" style="width: 50px" />&nbsp;mg/L
            </p>
          </div>
          <div class="set-up" id="set-up-2">
            <Icon type="md-color-fill" size="80" />
            <p>
              <i>标液2</i>&nbsp;&nbsp;&nbsp;&nbsp;
              <Input v-model="water2" size="small" style="width: 50px" />&nbsp;mg/L
            </p>
          </div>
          <div class="set-up" id="set-up-3">
            <Icon type="ios-color-fill-outline" size="80" />
            <p>
              <i>标液3</i>&nbsp;&nbsp;&nbsp;&nbsp;
              <Input v-model="water3" size="small" style="width: 50px" />&nbsp;mg/L
            </p>
          </div>
        </td>
        <td>{{ OD1 }}</td>
        <td>{{ RSD1 }}</td>
        <td>{{ process1 }}%</td>
        <td>
          <Button>开始校准</Button>
        </td>
      </tr>
      <tr>
        <td>{{ OD2 }}</td>
        <td>{{ RSD2 }}</td>
        <td>{{ process2 }}%</td>
        <td>
          <Button>开始校准</Button>
        </td>
      </tr>
      <tr>
        <td>{{ OD3 }}</td>
        <td>{{ RSD3 }}</td>
        <td>{{ process3 }}%</td>
        <td>
          <Button>开始校准</Button>
        </td>
      </tr>
    </tbody>
  </table>
</template>
<script>
export default {
  data() {
    return {
      method: "",
      water1: "0.3",
      water2: "0.5",
      water3: "0.4",
      multiple: "4",
      OD1: "0",
      OD2: "0",
      OD3: "0",
      RSD1: "0",
      RSD2: "0",
      RSD3: "0",
      process1: "0.00",
      process2: "0.00",
      process3: "0.00",
      columns4: [
        {
          type: "selection",
          width: 60,
          align: "center"
        },
        {
          title: "Name",
          key: "name"
        },
        {
          title: "Age",
          key: "age"
        },
        {
          title: "Address",
          key: "address"
        }
      ],
      data1: [
        {
          name: "John Brown",
          age: 18,
          address: "New York No. 1 Lake Park",
          date: "2016-10-03"
        },
        {
          name: "Jim Green",
          age: 24,
          address: "London No. 1 Lake Park",
          date: "2016-10-01"
        },
        {
          name: "Joe Black",
          age: 30,
          address: "Sydney No. 1 Lake Park",
          date: "2016-10-02"
        },
        {
          name: "Jon Snow",
          age: 26,
          address: "Ottawa No. 2 Lake Park",
          date: "2016-10-04"
        }
      ]
    };
  },
  methods: {
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
          return;
        }
      };
    }
  }
};
</script>

<style scoped>
.table td {
  height: 156px;
  line-height: 140px;
}
thead th,
.table td {
  text-align: center;
}
.dilution {
  margin-top: 120px;
}
.dilution p {
  margin-top: -80px;
  margin-left: -15px;
  font-size: 14px;
}
.auto,
.hand {
  margin-top: 50px;
}
.auto p,
.hand p {
  font-size: 14px;
}
.choose {
  height: 55px;
  margin-top: -40px;
}
.set-up p {
  margin-top: -80px;
  height: 80px;
}
</style>