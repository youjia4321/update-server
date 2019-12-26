<template>
  <div class="container">
    <div class="content">
      <Row>
        <i-Col span="8" v-for="item in cloumns" :key="item.id">
          <router-link :to="item.link">
            <div class="cloumns">
              <Card>
                <p slot="title">{{ item.label }}</p>
                <div style="text-align:center">
                  <img src="../../assets/logo/logo.png" />
                  <h3 style="font-size: 18px; color: gray">四川炜麒科技股份有限公司</h3>
                </div>
              </Card>
            </div>
          </router-link>
        </i-Col>
      </Row>
    </div>
  </div>
</template>
<script>
export default {
  name: "SysIndex",
  data() {
    return {
      cloumns: [],
    };
  },
  created() {
    this.getCloumns();
  },
  methods: {
    getCloumns() {
      this.cloumns = this.$service.cloumns();
    }
  }
};
</script>

<style scoped>
.ivu-col-span-8 {
  padding: 20px;
}
.cloumns {
  box-shadow: 7px 7px 7px #888888;
}
</style>>
