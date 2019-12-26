<template>
  <div class="protect">
    <Row>
      <i-Col span="8" class="menu">
        <Button class="btn" @click="show">
          <img src="../assets/set_up/waterpump.png" />&nbsp;&nbsp;诊断泵
        </Button>
      </i-Col>
      <i-Col span="8" class="menu">
        <Button class="btn" @click="show">
          <img src="../assets/set_up/waterswitch.png" />&nbsp;&nbsp;阀组诊断
        </Button>
      </i-Col>
      <i-Col span="8" class="menu">
        <Button class="btn" @click="show">
          <img src="../assets/set_up/internalProcess.png" />&nbsp;&nbsp;内部状态
        </Button>
      </i-Col>
      <i-Col span="8" class="menu">
        <Button class="btn" @click="show">
          <img src="../assets/set_up/clean.png" />&nbsp;&nbsp;清洗
        </Button>
      </i-Col>
      <i-Col span="8" class="menu">
        <Button class="btn" @click="show">
          <img src="../assets/set_up/rinse.png" />&nbsp;&nbsp;冲洗
        </Button>
      </i-Col>
      <i-Col span="8" class="menu">
        <Button class="btn" @click="show">
          <img src="../assets/set_up/UDisk.png" />&nbsp;&nbsp;导出日志
        </Button>
      </i-Col>
    </Row>
  </div>
</template>

<script>
export default {
  name: "SysProtect",
  methods: {
    show() {
      this.$Message.error("暂无此选项");
    }
  }
};
</script>

<style scoped>
.protect {
  height: 506px;
}
.protect .menu {
  height: 253px;
  /* border: 1px solid #dad6d6; */
  text-align: center;
  line-height: 253px;
}
img {
  width: 110px;
}
.btn {
  height: 150px;
  width: 197px;
  font-size: 14px;
  font-weight: 600;
  border: 1px solid #dadada;
}
</style>