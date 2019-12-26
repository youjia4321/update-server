<template>
  <div class="header">
    <div class="container">
      <router-link to="/">
        <div class="head-img">
          <img src="../assets/logo/logo.png" alt width="50px" />
        </div>
        <div class="head-title">&nbsp;&nbsp;WeiQI Management System</div>
      </router-link>
      <Menu mode="horizontal" theme="light" active-name="1" @on-select="showLogout">
        <Submenu name="1">
          <template slot="title">
            <Icon type="ios-folder" />系统服务
          </template>
          <MenuGroup title="服务">
            <MenuItem name="1-1">修改密码</MenuItem>
          </MenuGroup>
        </Submenu>
        <Submenu name="2">
          <template slot="title">
            <Icon type="ios-person" />系统管理员
          </template>
          <MenuGroup title="管理">
            <MenuItem name="2-1">退出系统</MenuItem>
            <MenuItem name="2-2" to="/system_Upload">上传文件</MenuItem>
          </MenuGroup>
        </Submenu>
      </Menu>
      <!-- 修改密码 -->
      <Modal v-model="modalChange" title="修改密码" width="300" :footer-hide="true">
        <Form ref="formCustom" :model="formCustom" :rules="ruleCustom">
          <FormItem prop="passwd">
            <i-Input type="password" v-model="formCustom.passwd" placeholder="输入新密码">
              <Icon type="ios-lock-outline" slot="prepend"></Icon>
            </i-Input>
          </FormItem>
          <FormItem prop="passwdCheck">
            <i-Input
              type="password"
              v-model="formCustom.passwdCheck"
              placeholder="确认新密码"
              @keyup.enter.native="handleSubmit('formCustom')"
            >
              <Icon type="ios-lock-outline" slot="prepend"></Icon>
            </i-Input>
          </FormItem>
          <FormItem>
            <Button type="primary" @click="handleSubmit('formCustom')">提交</Button>
            <Button @click="handleReset('formCustom')" style="margin-left: 8px">重置</Button>
          </FormItem>
        </Form>
      </Modal>
      <!-- 退出系统 -->
      <Modal v-model="modaLogout" width="300">
        <p slot="header" style="color:#f60;">
          <Icon type="ios-information-circle"></Icon>
          <span>&nbsp;&nbsp;系统提示</span>
        </p>
        <p>你确定要退出登录吗？</p>
        <div slot="footer">
          <Button type="error" size="large" long :loading="modal_loading" @click="handleLogout">确认</Button>
        </div>
      </Modal>
    </div>
  </div>
</template>
<script>
export default {
  name: "SysHeader",
  data() {
    const validatePass = (rule, value, callback) => {
      if (value === "") {
        callback(new Error("请输入密码"));
      } else {
        if (this.formCustom.passwdCheck !== "") {
          // 对第二个密码框单独验证
          this.$refs.formCustom.validateField("passwdCheck");
        }
        callback();
      }
    };
    const validatePassCheck = (rule, value, callback) => {
      if (value === "") {
        callback(new Error("请再次输入密码"));
      } else if (value !== this.formCustom.passwd) {
        callback(new Error("两次密码不一致！"));
      } else {
        callback();
      }
    };
    return {
      modalChange: false,
      modal_loading: false,
      modaLogout: false,
      formCustom: {
        passwd: "",
        passwdCheck: ""
      },
      ruleCustom: {
        passwd: [{ validator: validatePass, trigger: "blur" }],
        passwdCheck: [{ validator: validatePassCheck, trigger: "blur" }]
      }
    };
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
    // 修改密码
    handleSubmit(name) {
      this.$refs[name].validate(valid => {
        if (valid) {
          let user = JSON.parse(sessionStorage.getItem("user"));
          this.$http
            .modifyPwd(
              user.username,
              this.formCustom.passwdCheck,
              this.getCookie("csrftoken")
            )
            .then(resp => {
              if (resp.data.msg === "Success!") {
                var obj = {
                  username: user.username,
                  password: this.formCustom.passwdCheck
                };
                sessionStorage.setItem("user", JSON.stringify(obj));
                this.$Message.success("Success to modify password!");
                this.modalChange = false;
              } else {
                this.modalChange = false;
                this.$Message.error(resp.data.msg);
              }
            });
        } else {
          this.$Message.error("Fail!");
        }
      });
    },
    // 重置表单
    handleReset(formName) {
      this.$refs[formName].resetFields();
    },
    showLogout(name) {
      if (name === "2-1") {
        this.modaLogout = true;
      } else if (name === "1-1") {
        this.modalChange = true;
      }
    },
    // 退出系统
    handleLogout() {
      this.modal_loading = true;
      this.$http.userLogout().then(resp => {
        if (resp.data.msg === "Success!") {
          this.modal_loading = false;
          this.modaLogout = false;
          this.$router.push({ name: "systemLogin" });
          this.$Message.success(resp.data.msg);
        }
      });
    }
  }
};
</script>

<style scoped>
.header {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 999;
  background: #babdc1;
  min-width: 700px;
}
.container {
  background: #babdc1;
}
.ivu-menu-light {
  background: #babdc1;
  float: right;
}
.head-title {
  float: left;
  font-size: 20px;
  line-height: 60px;
  color: #fff;
  font-family: sans-serif;
}
.head-img {
  float: left;
  height: 50px;
  padding-top: 5px;
  /* margin-left: 20px; */
}
.ivu-menu-item,
.ivu-menu-submenu {
  color: #4e4e4e !important;
}
</style>