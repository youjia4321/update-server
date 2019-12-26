<template>
  <div class="history">
    <Table border height="460" :columns="columns1" :data="data2"></Table>
    <Button class="btn">查询</Button>
  </div>
</template>
<script>
export default {
  data() {
    return {
      columns1: [
        {
          title: "TP测量时间",
          key: "date"
        },
        {
          title: "TP(mg/L)",
          key: "age"
        },
        {
          title: "相对吸光度",
          key: "address"
        }
      ],
      data2: [
        {
          age: 18,
          address: "New York No. 1 Lake Park",
          date: "2016-10-03"
        },
        {
          age: 24,
          address: "London No. 1 Lake Park",
          date: "2016-10-01"
        },
        {
          age: 30,
          address: "Sydney No. 1 Lake Park",
          date: "2016-10-02"
        },
        {
          age: 26,
          address: "Ottawa No. 2 Lake Park",
          date: "2016-10-04"
        },
        {
          age: 18,
          address: "New York No. 1 Lake Park",
          date: "2016-10-03"
        },
        {
          age: 24,
          address: "London No. 1 Lake Park",
          date: "2016-10-01"
        },
        {
          age: 30,
          address: "Sydney No. 1 Lake Park",
          date: "2016-10-02"
        },
        {
          age: 26,
          address: "Ottawa No. 2 Lake Park",
          date: "2016-10-05"
        },
        {
          age: 26,
          address: "Ottawa No. 2 Lake Park",
          date: "2016-10-04"
        },
        {
          age: 26,
          address: "Ottawa No. 2 Lake Park",
          date: "2016-10-03"
        },
        {
          age: 26,
          address: "Ottawa No. 2 Lake Park",
          date: "2016-10-02"
        },
        {
          age: 26,
          address: "Ottawa No. 2 Lake Park",
          date: "2016-10-01"
        }
      ]
    };
  }
};
</script>

<style scoped>
.btn {
  float: right;
  margin-right: 2%;
  margin-top: 5px;
  border: 1px solid #dadada;
}
</style>
