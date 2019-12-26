<template>
  <div class="main">
    <router-view name="header"></router-view>
    <div class="container">
      <div class="content">
        <Row>
          <i-Col span="6" v-for="item in equipments" :key="item.id">
            <div class="equip" @click="goToEquipment(item.id)">
              <Card>
                <p slot="title">{{ item.label }}</p>
                <div style="text-align:center">
                  <img src="../../assets/logo/logo.png" width="50px" />
                  <h3 style="font-size: 15px; color: gray">四川炜麒科技股份有限公司</h3>
                </div>
              </Card>
            </div>
          </i-Col>
        </Row>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "SysReagent",
  data() {
    return {
      equipments: []
    };
  },
  mounted() {
    this.getEquipments();
  },
  methods: {
    getEquipments() {
      this.equipments = this.$service.equipments();
    },
    goToEquipment(id) {
      this.$router.push({
        name: "system_reagent",
        query: { equipId: id }
      });
    }
  }
};
</script>

<style scoped>
.ivu-col-span-6 {
  padding: 30px;
}
.equip {
  cursor: pointer;
  box-shadow: 7px 7px 7px #888888;
}
</style>