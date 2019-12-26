<template>
  <!-- 登陆页面 -->
  <div class="formIn">
    <Card
      :style="{width: '300px', border: 'solid 1px rgb(239, 220, 220)', borderRadius: '4px', margin: '150px auto' }"
    >
      <p slot="title">
        <img src="../../assets/logo/logo.png" width="25px;" />
      </p>
      <p slot="extra">
        <Icon type="ios-loop-strong"></Icon>WeiQi Management System
      </p>
      <Form ref="formInline" :model="formInline" :rules="ruleInline">
        <FormItem prop="user">
          <i-Input type="text" v-model="formInline.user" placeholder="请输入登录账户">
            <Icon type="ios-person" slot="prepend" size="16"></Icon>
          </i-Input>
        </FormItem>
        <FormItem prop="password">
          <i-Input
            type="password"
            v-model="formInline.password"
            placeholder="请输入登录密码"
            @keyup.enter.native="handleSubmit('formInline')"
          >
            <Icon type="ios-lock" slot="prepend" size="16"></Icon>
          </i-Input>
        </FormItem>
        <FormItem>
          <div class="prompt" style="float: left">
            <Checkbox v-model="checked">记住密码</Checkbox>
          </div>
          <div class="prompt" style="float: right">
            <a>Forgot password?</a>
          </div>
        </FormItem>
        <FormItem>
          <Button type="primary" @click="handleSubmit('formInline')">登录</Button>
          <Button @click="handleReset('formInline')" style="margin-left: 8px">重置</Button>
        </FormItem>
      </Form>
    </Card>
  </div>
</template>

<script>
export default {
  name: "SysLogin",
  data() {
    return {
      checked: false,
      obj: {
        margin: "0 5px 0",
        background: "#fbfbfb",
        overflow: "hidden",
        fontSize: "14px"
      },
      formInline: {
        user: "",
        password: ""
      },
      ruleInline: {
        user: [
          {
            required: true,
            message: "请填写登录账户",
            trigger: "blur"
          }
        ],
        password: [
          {
            required: true,
            message: "请填写登录密码",
            trigger: "blur"
          }
        ]
      }
    };
  },
  mounted() {
    let userinfo = localStorage.getItem("userInfo");
    if (userinfo) {
      // 如果存在就自动填写用户信息
      userinfo = JSON.parse(localStorage.getItem("userInfo"));
      this.formInline.user = userinfo.username;
      this.formInline.password = userinfo.password;
      this.checked = userinfo.checked;
    }
  },
  methods: {
    // post请求需要获取csrftoken
    getCookie(name) {
      var value = "; " + document.cookie;
      var parts = value.split("; " + name + "=");
      if (parts.length === 2)
        return parts
          .pop()
          .split(";")
          .shift();
    },
    handleSubmit(name) {
      this.$refs[name].validate(valid => {
        if (valid) {
          this.$http
            .userLogin(
              this.formInline.user,
              this.formInline.password,
              this.getCookie("csrftoken")
            )
            .then(resp => {
              if (resp.data.msg === "Success!") {
                if (this.checked == true) {
                  let userinfo = {
                    username: this.formInline.user,
                    password: this.formInline.password,
                    checked: true
                  };
                  localStorage.setItem("userInfo", JSON.stringify(userinfo));
                } else {
                  localStorage.removeItem("userInfo");
                }
                this.$Message.success("Success to login!");
                var obj = {
                  username: this.formInline.user,
                  password: this.formInline.password,
                  checked: true
                };
                sessionStorage.setItem("manageuser", JSON.stringify(obj));
                this.$router.push({
                  path: "/system_Index"
                });
              } else {
                this.$Message.error(resp.data.msg);
              }
            })
            .catch(() => {
              this.$Message.error("服务器出错，稍后再试");
            });
        } else {
          this.formInline.password = "";
          this.$Message.error("Fail!");
        }
      });
    },
    handleReset(formName) {
      this.$refs[formName].resetFields();
      var obj = {
        username: this.formInline.user,
        password: this.formInline.password
      };
      sessionStorage.setItem("user", JSON.stringify(obj));
      this.$router.push({ path: "/system_Login" });
    }
  }
};
</script>

<style scoped>
.formIn {
  padding: 50px;
}
.ivu-card-extra p {
  font-weight: 600;
  font-size: 16px;
}
.ivu-card-body {
  background: #efefef;
}
.ivu-form-item {
  margin-bottom: 30px;
}
.prompt {
  font-size: 13px;
  font-weight: 600;
}
</style>
