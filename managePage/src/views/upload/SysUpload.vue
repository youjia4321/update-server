<template>
  <div class="main">
    <router-view name="header"></router-view>
    <div class="container">
      <div class="content">
        <Tag size="large" color="primary">选择文件类型</Tag>&nbsp;
        <Button type="success" ghost icon="md-add-circle" @click="typeModal = true">添加设备类型</Button>&nbsp;&nbsp;
        <Modal v-model="typeModal" @on-ok="addType()" @on-visible-change="clearTypeInfo">
          <p slot="header" style="color:#f60">
            <Icon type="ios-information-circle"></Icon>
            <span>&nbsp;设备类型</span>
          </p>
          <Tag color="blue">添加设备类型</Tag>
          <br />
          <Input v-model="typeAdd" style="width: 200px" />
        </Modal>
        <Button type="success" ghost icon="md-add-circle" @click="equipModal = true">添加设备信息</Button>&nbsp;&nbsp;
        <Modal v-model="equipModal" @on-ok="addEquipment()" @on-visible-change="clearEquipInfo">
          <p slot="header" style="color:#f60">
            <Icon type="ios-information-circle"></Icon>
            <span>&nbsp;设备信息</span>
          </p>
          <Tag color="blue">设备类型</Tag>
          <br />
          <Select v-model="equipType" style="width:200px; margin-bottom: 20px;">
            <Option v-for="item in typeList" :value="item.value" :key="item.value">{{ item.label }}</Option>
          </Select>
          <br />
          <Tag color="blue">设备编号</Tag>
          <br />
          <Input v-model="equipID" style="width: 200px" />
        </Modal>
        <Button type="error" ghost icon="md-settings" @click="manageModal1 = true">设备类型管理</Button>&nbsp;&nbsp;
        <Modal v-model="manageModal1">
          <p slot="header" style="color:#f60;">
            <Icon type="md-settings"></Icon>
            <span>&nbsp;设备类型管理</span>
          </p>
          <div style="text-align:center">
            <el-table
              ref="multipleTable1"
              :data="typeData"
              :border="true"
              size="mini"
              tooltip-effect="dark"
            >
              <el-table-column label="设备类型">
                <template slot-scope="scope">{{ scope.row.type }}</template>
              </el-table-column>
              <el-table-column width="100">
                <template slot="header">操作</template>
                <template slot-scope="scope">
                  <el-button type="text" @click="deleteType(scope.row)" size="small">删除</el-button>
                </template>
              </el-table-column>
            </el-table>
          </div>
          <div slot="footer"></div>
        </Modal>
        <Button type="error" ghost icon="md-settings" @click="manageModal2 = true">设备信息管理</Button>&nbsp;&nbsp;
        <Modal v-model="manageModal2">
          <p slot="header" style="color:#f60;">
            <Icon type="md-settings"></Icon>
            <span>&nbsp;设备信息管理</span>
          </p>
          <div style="text-align:center">
            <el-table
              ref="multipleTable2"
              :data="equipData.filter(data => !search || data.equip_id.toLowerCase().includes(search.toLowerCase()))"
              :border="true"
              height="300px"
              size="mini"
              tooltip-effect="dark"
              @selection-change="handleSelectionChange"
            >
              <el-table-column type="selection" width="55"></el-table-column>
              <el-table-column label="设备编号">
                <template slot-scope="scope">{{ scope.row.equip_id }}</template>
              </el-table-column>
              <el-table-column align="right">
                <template slot="header">
                  <el-input
                    v-model="search"
                    prefix-icon="el-icon-search"
                    size="mini"
                    placeholder="输入关键字搜索"
                  />
                </template>
                <template slot-scope="scope">
                  <el-button type="text" @click="deleteEquipment(scope.row)" size="small">删除</el-button>
                </template>
              </el-table-column>
            </el-table>
          </div>
          <div slot="footer">
            <el-button type="danger" @click="deleteEquipments">删除选择选项（{{ count }}）</el-button>
          </div>
        </Modal>
        <br />
        <Select v-model="type" style="width:200px; margin-bottom: 20px;" @on-change="changeType()">
          <Option v-for="item in typeList" :value="item.value" :key="item.value">{{ item.label }}</Option>
        </Select>
        <br />
        <Tag size="large" color="primary">选择上传文件</Tag>
        <br />
        <Upload
          multiple
          type="drag"
          ref="upload"
          :before-upload="handleUpload"
          :on-success="uploadSuccess"
          :on-error="uploadError"
          :action="api+'/uploadFiles'"
          :data="data"
          :show-upload-list="true"
        >
          <div style="padding: 20px 0">
            <Icon type="ios-cloud-upload" size="52" style="color: #3399ff"></Icon>
            <p>Click or drag files here to upload</p>
          </div>
        </Upload>
      </div>
      <SysSearch ref="child"></SysSearch>
    </div>
  </div>
</template>

<script>
import SysSearch from "@/components/upload/SysSearch";

export default {
  data() {
    return {
      api: this.api,
      type: "",
      typeList: [],
      data: {},
      typeModal: false,
      equipModal: false,
      manageModal1: false,
      manageModal2: false,
      equipType: "",
      equipID: "",
      typeAdd: "",
      typeData: [],
      equipData: [],
      choose: [],
      count: 0,
      search: ""
    };
  },
  inject: ["reload"],
  components: {
    SysSearch
  },
  created() {
    this.getTypes();
    this.getEquipments();
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
    getEquipments() {
      this.$http.responseEquipment().then(resp => {
        if (resp.result.code == "200") {
          this.equipData = resp.result.data;
        }
      });
    },
    getTypes() {
      this.$http.responseType().then(resp => {
        if (resp.result.code === "200") {
          this.typeList = resp.result.data;
          this.type = this.typeList[0].value;
          this.equipType = this.typeList[0].value;
          this.data = { type: this.type };
          this.typeData = resp.result.type;
        } else if (resp.result.code === "400") {
          this.typeList = resp.result.data;
          this.type = this.typeList[0].value;
          this.equipType = this.typeList[0].value;
          this.typeData = resp.result.type;
        }
      });
    },
    changeType() {
      this.data = { type: this.type };
    },
    handleUpload() {
      if (this.type !== "暂无设备类型") {
        return true;
      } else {
        this.$Message.error("请先添加设备类型");
        return false;
      }
    },
    uploadSuccess(res) {
      //上传成功
      if (res.result.code == 200) {
        this.$Message.info(res.result.msg);
        this.$refs.child.changeType();
        this.$refs.child.changeSingleTypeEquipments();
      }
    },
    uploadError(error) {
      this.$Message.info(error);
    },
    addType() {
      if (
        this.typeAdd.trim().indexOf(" ") == -1 &&
        this.typeAdd.trim().length !== 0
      ) {
        this.$http
          .createTag(this.typeAdd, this.getCookie("csrftoken"))
          .then(resp => {
            if (resp.result.code === "200") {
              this.$Message.success("添加成功");
              this.typeAdd = "";
              this.getTypes();
              this.$refs.child.getTypes();
              // this.reload();
            } else {
              this.$Message.error(resp.result.msg);
              this.typeAdd = "";
            }
          });
      } else {
        this.$Message.error("检查设备类型是否输入正确（不要包含空格）");
      }
    },
    addEquipment() {
      if (
        this.equipID.trim().indexOf(" ") == -1 &&
        this.equipID.trim().length !== 0
      ) {
        this.$http
          .createEquipment(
            this.equipType,
            this.equipID,
            this.getCookie("csrftoken")
          )
          .then(resp => {
            if (resp.result.code === "200") {
              this.$Message.success("添加成功");
              this.equipID = "";
              this.getEquipments();
              this.$refs.child.getSingleTypeEquipments();
              // this.reload();
            } else {
              this.$Message.error(resp.result.msg);
              this.equipID = "";
            }
          });
      } else {
        this.$Message.error("检查设备编号是否输入正确（不要包含空格）");
      }
    },
    clearTypeInfo(bool) {
      if (bool === false) {
        this.typeAdd = "";
      }
    },
    clearEquipInfo(bool) {
      if (bool === false) {
        this.equipID = "";
      }
    },
    deleteType(row) {
      this.manageModal1 = false;
      this.$confirm("此操作将永久删除该设备类型及关联数据, 是否继续?", "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning"
      }).then(() => {
        this.$http
          .deleteType(row.type, this.getCookie("csrftoken"))
          .then(resp => {
            if (resp.result.code === "200") {
              this.reload();
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
    deleteEquipment(row) {
      this.manageModal2 = false;
      this.$confirm("此操作将永久删除该设备及关联数据, 是否继续?", "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning"
      }).then(() => {
        this.$http
          .deleteEquipment(row.equip_id, this.getCookie("csrftoken"))
          .then(resp => {
            if (resp.result.code === "200") {
              this.$message({
                type: "success",
                message: "删除成功!"
              });
              this.getEquipments();
              this.$refs.child.getSingleTypeEquipments();
            } else {
              this.$message({
                type: "error",
                message: resp.result.msg
              });
            }
          });
      });
    },
    deleteEquipments() {
      this.manageModal2 = false;
      if (this.count !== 0) {
        this.$confirm(
          "此操作将永久删除【已选择（" + this.count + "）】此设备, 是否继续?",
          "提示",
          {
            confirmButtonText: "确定",
            cancelButtonText: "取消",
            type: "warning"
          }
        ).then(() => {
          this.$http
            .deleteEquipments(this.choose, this.getCookie("csrftoken"))
            .then(resp => {
              if (resp.result.code === "200") {
                this.getEquipments();
                this.$refs.child.getSingleTypeEquipments();
                this.$message({
                  type: "success",
                  message: "删除成功!"
                });
                this.choose = [];
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
    handleSelectionChange(val) {
      this.choose = val;
      this.count = this.choose.length;
    }
  }
};
</script>

<style>
</style>