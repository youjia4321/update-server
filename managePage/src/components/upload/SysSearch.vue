<template>
  <div class="main">
    <hr style="border-color: #000" />
    <Tabs>
      <TabPane label="设备类型文件" icon="ios-folder">
        <div class="equipemnt-table">
          <Select
            v-model="type2"
            style="width:200px; margin-bottom: 20px;"
            @on-change="changeType()"
          >
            <Option v-for="item in typeList" :value="item.value" :key="item.value">{{ item.label }}</Option>
          </Select>&nbsp;&nbsp;&nbsp;
          <br />
          <el-table
            ref="multipleTable"
            :data="tableData"
            :border="true"
            size="mini"
            height="300px"
            tooltip-effect="dark"
            style="width: 100%"
            @selection-change="handleSelectionChange"
          >
            <el-table-column type="selection" width="55"></el-table-column>
            <el-table-column label="日期" width="200">
              <template slot-scope="scope">{{ scope.row.date }}</template>
            </el-table-column>
            <el-table-column prop="filename" label="文件名" show-overflow-tooltip></el-table-column>
            <el-table-column prop="position" label="文件储存地址" show-overflow-tooltip></el-table-column>
            <el-table-column
              prop="updated"
              label="是否可更新"
              width="120"
              :filters="[{ text: 'True', value: 'True' }, { text: 'False', value: 'False' }]"
              :filter-method="filterUpdated"
            ></el-table-column>
            <el-table-column prop="version" label="版本号"></el-table-column>
            <el-table-column fixed="right" label="操作" width="100">
              <template slot-scope="scope">
                <el-button @click="editFile(scope.row)" type="text" size="small">编辑</el-button>
                <el-button type="text" size="small" @click="deleteFile(scope.row)">删除</el-button>
              </template>
            </el-table-column>
          </el-table>
          <div style="margin-top: 30px; margin-bottom: 20px;">
            <el-button type="info" @click="toggleSelection()">取消选择（{{ countGlobal }}）</el-button>
            <el-button type="primary" @click="editFiles">编辑选择选项（{{ countGlobal }}）</el-button>
            <el-button type="danger" @click="deleteFiles">删除选择选项（{{ countGlobal }}）</el-button>
            <el-button type="success" @click="clearFilter">清除所有过滤器</el-button>
          </div>
        </div>
      </TabPane>
      <TabPane label="单设备文件信息" icon="ios-information-circle">
        <div class="equipemnt-table">
          <Select
            v-model="type"
            style="width:200px; margin-bottom: 20px;"
            @on-change="changeSingleType()"
          >
            <Option v-for="item in typeList" :value="item.value" :key="item.value">{{ item.label }}</Option>
          </Select>&nbsp;&nbsp;&nbsp;
          <Select
            v-model="type1"
            style="width:200px; margin-bottom: 20px;"
            @on-change="changeSingleTypeEquipments()"
          >
            <Option v-for="item in equipList" :value="item.value" :key="item.value">{{ item.label }}</Option>
          </Select>&nbsp;&nbsp;&nbsp;
          <Button
            style="margin-bottom: 20px;"
            title="设备是否可更新"
            @click="changeSingleTypeEquipmentStatus"
          >{{ isEquipUpdate }}</Button>
          <br />
          <el-table
            ref="multipleSingleTable"
            :data="tableSingleData"
            :border="true"
            size="mini"
            height="300px"
            tooltip-effect="dark"
            style="width: 100%"
            @selection-change="handleSingleSelectionChange"
          >
            <el-table-column type="selection" width="55"></el-table-column>
            <el-table-column label="日期" width="200">
              <template slot-scope="scope">{{ scope.row.date }}</template>
            </el-table-column>
            <el-table-column prop="filename" label="文件名" show-overflow-tooltip></el-table-column>
            <el-table-column prop="position" label="文件储存地址" show-overflow-tooltip></el-table-column>
            <el-table-column
              prop="updated"
              label="是否可更新"
              width="120"
              :filters="[{ text: 'True', value: 'True' }, { text: 'False', value: 'False' }]"
              :filter-method="filterSingleUpdated"
            ></el-table-column>
            <el-table-column prop="version" label="版本号"></el-table-column>
            <el-table-column fixed="right" label="操作" width="100">
              <template slot-scope="scope">
                <el-button @click="editSingleFile(scope.row)" type="text" size="small">编辑</el-button>
                <el-button type="text" size="small" @click="deleteSingleFile(scope.row)">删除</el-button>
              </template>
            </el-table-column>
          </el-table>
          <div style="margin-top: 30px; margin-bottom: 20px;">
            <el-button type="info" @click="toggleSingleSelection()">取消选择（{{ countSingle }}）</el-button>
            <el-button type="primary" @click="editSingleFiles">编辑选择选项（{{ countSingle }}）</el-button>
            <el-button type="danger" @click="deleteSingleFiles">删除选择选项（{{ countSingle }}）</el-button>
            <el-button type="success" @click="clearSingleFilter">清除所有过滤器</el-button>
          </div>
        </div>
      </TabPane>
    </Tabs>
  </div>
</template>

<script>
export default {
  data() {
    return {
      type: "",
      type1: "",
      type2: "",
      typeList: [],
      equipList: [],
      tableSingleData: [],
      tableData: [],
      //   选择的数据
      multipleSelection: [],
      countGlobal: 0,
      multipleSingleSelection: [],
      countSingle: 0,

      isEquipUpdate: ""
    };
  },
  created() {
    this.getTypes();
  },
  methods: {
    getCookie(name) {
      var value = "; " + document.cookie;
      var parts = value.split("; " + name + "=");
      if (parts.length === 2)
        return parts
          .pop()
          .split(";")
          .shift();
    },
    getTypes() {
      this.$http.responseType().then(resp => {
        if (resp.result.code === "200") {
          this.typeList = resp.result.data;
          this.type = this.typeList[0].value;
          this.type2 = this.typeList[0].value;
          this.getSingleTypeEquipments();
          this.changeType();
        }
      });
    },
    getSingleTypeEquipments() {
      this.$http
        .responseTypeEquipment(this.type, this.getCookie("csrftoken"))
        .then(resp => {
          if (resp.result.code === "200") {
            this.equipList = resp.result.data;
            this.type1 = this.equipList[0].value;
            this.changeSingleTypeEquipments();
          } else if (resp.result.code === "400") {
            this.equipList = resp.result.data;
            this.type1 = this.equipList[0].value;
            this.tableSingleData = [];
          } else {
            this.$Message.error(resp.result.msg);
          }
        });
    },
    changeType() {
      this.$http
        .responseTable(this.type2, this.getCookie("csrftoken"))
        .then(resp => {
          if (resp.result.code === "200") {
            this.tableData = resp.result.data;
          } else if (resp.result.code === "400") {
            this.tableData = resp.result.data;
          }
        });
    },
    changeSingleType() {
      this.getSingleTypeEquipments();
    },
    changeSingleTypeEquipments() {
      this.isEquipUpdate = false;
      this.$http
        .responseSingleTable(this.type, this.type1, this.getCookie("csrftoken"))
        .then(resp => {
          if (resp.result.code === "200") {
            this.isEquipUpdate = resp.result.is_update;
            this.tableSingleData = resp.result.data;
          } else if (resp.result.code === "400") {
            this.tableSingleData = resp.result.data;
          } else {
            this.$Message.error(resp.result.msg);
          }
        });
    },
    changeSingleTypeEquipmentStatus() {
      this.$http
        .changeStatus(this.type, this.type1, this.getCookie("csrftoken"))
        .then(resp => {
          if (resp.result.code === "200") {
            this.isEquipUpdate = resp.result.is_update;
          } else {
            this.$Message.error(resp.result.msg);
          }
        });
    },
    toggleSelection(rows) {
      if (rows) {
        rows.forEach(row => {
          this.$refs.multipleTable.toggleRowSelection(row);
        });
      } else {
        this.$refs.multipleTable.clearSelection();
      }
    },
    toggleSingleSelection(rows) {
      if (rows) {
        rows.forEach(row => {
          this.$refs.multipleSingleTable.toggleRowSelection(row);
        });
      } else {
        this.$refs.multipleSingleTable.clearSelection();
      }
    },
    handleSelectionChange(val) {
      this.multipleSelection = val;
      this.countGlobal = this.multipleSelection.length;
    },
    handleSingleSelectionChange(val) {
      this.multipleSingleSelection = val;
      this.countSingle = this.multipleSingleSelection.length;
    },
    filterUpdated(value, row) {
      return row.updated === value;
    },
    filterSingleUpdated(value, row) {
      return row.updated === value;
    },
    clearFilter() {
      this.$refs.multipleTable.clearFilter();
    },
    clearSingleFilter() {
      this.$refs.multipleSingleTable.clearFilter();
    },
    deleteFile(row) {
      this.$confirm("此操作将永久删除该类型文件, 是否继续?", "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning"
      }).then(() => {
        this.$http
          .deleteGlobalFile(
            this.type2,
            row.filename,
            this.getCookie("csrftoken")
          )
          .then(resp => {
            if (resp.result.code === "200") {
              this.changeType();
              this.changeSingleTypeEquipments();
              this.$message({
                type: "success",
                message: "删除成功!"
              });
            } else {
              this.$message({
                type: "error",
                message: resp.result.msg
              });
            }
          });
      });
    },
    deleteFiles() {
      if (this.countGlobal !== 0) {
        this.$confirm(
          "此操作将永久删除【已选择（" +
            this.countGlobal +
            "）】该类型文件, 是否继续?",
          "提示",
          {
            confirmButtonText: "确定",
            cancelButtonText: "取消",
            type: "warning"
          }
        ).then(() => {
          // console.log(this.multipleSelection);
          this.$http
            .deleteGlobalFiles(
              this.type2,
              this.multipleSelection,
              this.getCookie("csrftoken")
            )
            .then(resp => {
              if (resp.result.code === "200") {
                this.changeType();
                this.changeSingleTypeEquipments();
                this.$message({
                  type: "success",
                  message: "删除成功!"
                });
              } else {
                this.$message({
                  type: "error",
                  message: resp.result.msg
                });
              }
            });
        });
      } else {
        this.$message({
          type: "error",
          message: "未选择文件"
        });
      }
    },
    editFile(row) {
      var msg = "";
      if (row.updated === "True") {
        msg = "此操作将文件设置为不可更新, 是否继续?";
      } else {
        msg = "此操作将文件设置为可更新, 是否继续?";
      }
      this.$confirm(msg, "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning"
      }).then(() => {
        this.$http
          .editGlobalFile(this.type2, row.filename, this.getCookie("csrftoken"))
          .then(resp => {
            if (resp.result.code === "200") {
              this.changeType();
              this.$message({
                type: "success",
                message: "设置成功!"
              });
            } else {
              this.$message({
                type: "error",
                message: resp.result.msg
              });
            }
          });
      });
    },
    editFiles() {
      if (this.countGlobal !== 0) {
        this.$confirm(
          "此操作将设置文件（可更新->不可更新，不可更新->可更新）已选择（" +
            this.countGlobal +
            "）文件, 是否继续?",
          "提示",
          {
            confirmButtonText: "确定",
            cancelButtonText: "取消",
            type: "warning"
          }
        ).then(() => {
          this.$http
            .editGlobalFiles(
              this.type2,
              this.multipleSelection,
              this.getCookie("csrftoken")
            )
            .then(resp => {
              if (resp.result.code === "200") {
                this.changeType();
                this.$message({
                  type: "success",
                  message: "设置成功!"
                });
              } else {
                this.$message({
                  type: "error",
                  message: resp.result.msg
                });
              }
            });
        });
      } else {
        this.$message({
          type: "error",
          message: "未选择文件"
        });
      }
    },
    deleteSingleFile(row) {
      this.$confirm("此操作将永久删除该设备文件, 是否继续?", "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning"
      }).then(() => {
        this.$http
          .deleteSingleFile(
            this.type,
            this.type1,
            row.filename,
            this.getCookie("csrftoken")
          )
          .then(resp => {
            if (resp.result.code === "200") {
              this.changeSingleTypeEquipments();
              this.$message({
                type: "success",
                message: "删除成功!"
              });
            } else {
              this.$message({
                type: "error",
                message: resp.result.msg
              });
            }
          });
      });
    },
    deleteSingleFiles() {
      if (this.countSingle !== 0) {
        this.$confirm(
          "此操作将永久删除【已选择（" +
            this.countSingle +
            "）】该设备文件, 是否继续?",
          {
            confirmButtonText: "确定",
            cancelButtonText: "取消",
            type: "warning"
          }
        ).then(() => {
          this.$http
            .deleteSingleFiles(
              this.type,
              this.type1,
              this.multipleSingleSelection,
              this.getCookie("csrftoken")
            )
            .then(resp => {
              if (resp.result.code === "200") {
                this.changeSingleTypeEquipments();
                this.$message({
                  type: "success",
                  message: "删除成功!"
                });
              } else {
                this.$message({
                  type: "error",
                  message: resp.result.msg
                });
              }
            });
        });
      } else {
        this.$message({
          type: "error",
          message: "未选择文件"
        });
      }
    },
    editSingleFile(row) {
      var msg = "";
      if (row.updated === "True") {
        msg = "此操作将文件设置为不可更新, 是否继续?";
      } else {
        msg = "此操作将文件设置为可更新, 是否继续?";
      }
      this.$confirm(msg, "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning"
      }).then(() => {
        this.$http
          .editSingleFile(
            this.type,
            this.type1,
            row.filename,
            this.getCookie("csrftoken")
          )
          .then(resp => {
            if (resp.result.code === "200") {
              this.changeSingleTypeEquipments();
              this.$message({
                type: "success",
                message: "设置成功!"
              });
            } else {
              this.$message({
                type: "error",
                message: resp.result.msg
              });
            }
          });
      });
    },
    editSingleFiles() {
      if (this.countSingle !== 0) {
        this.$confirm(
          "此操作将设置文件（可更新->不可更新，不可更新->可更新）已选择（" +
            this.countSingle +
            "）文件, 是否继续?",
          "提示",
          {
            confirmButtonText: "确定",
            cancelButtonText: "取消",
            type: "warning"
          }
        ).then(() => {
          this.$http
            .editSingleFiles(
              this.type,
              this.type1,
              this.multipleSingleSelection,
              this.getCookie("csrftoken")
            )
            .then(resp => {
              if (resp.result.code === "200") {
                this.changeSingleTypeEquipments();
                this.$message({
                  type: "success",
                  message: "设置成功!"
                });
              } else {
                this.$message({
                  type: "error",
                  message: resp.result.msg
                });
              }
            });
        });
      } else {
        this.$message({
          type: "error",
          message: "未选择文件"
        });
      }
    },
    changeStatus() {}
  }
};
</script>

<style>
</style>