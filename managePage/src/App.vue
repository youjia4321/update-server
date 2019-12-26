<template>
  <div id="main">
    <div class="layout">
      <router-view name="header"></router-view>
      <router-view v-if="isRouterAlive"></router-view>
      <router-view name="footer"></router-view>
    </div>
    <div class="form-login">
      <router-view name="login"></router-view>
    </div>
  </div>
</template>

<script>
export default {
  name: "SystemApp",
  provide() {
    return {
      reload: this.reload
    };
  },
  data() {
    return {
      isRouterAlive: true
    };
  },
  methods: {
    reload() {
      this.isRouterAlive = false;
      this.$nextTick(() => {
        this.isRouterAlive = true;
      });
    }
  }
};
</script>

<style lang="scss">
.content {
  margin: 120px 0 50px 0;
  min-width: 600px;
}
.el-tabs--left .el-tabs__item.is-left {
  text-align: right;
  height: 80px;
  line-height: 80px;
  border: 1px solid #e6e4e4;
}
p .ivu-input {
  border: 1px solid #676666 !important;
}
html,
body,
div,
span,
h1,
h2,
h3,
h4,
h5,
h6,
p,
pre,
a,
abbr,
acronym,
address,
big,
cite,
code,
del,
dfn,
em,
img,
ins,
kbd,
q,
s,
samp,
small,
strike,
strong,
sub,
sup,
tt,
var,
b,
u,
i,
center,
dl,
dt,
dd,
ol,
ul,
li,
fieldset,
form,
label,
legend,
table,
caption,
tbody,
tfoot,
thead,
tr,
th,
td,
article,
aside,
canvas,
details,
embed,
figure,
figcaption,
footer,
header,
hgroup,
menu,
nav,
output,
ruby,
section,
summary,
time,
mark,
audio,
video {
  margin: 0;
  padding: 0;
  border: 0;
  font-size: 100%;
  font: inherit;
  vertical-align: baseline;
}
// HTML5 display-role reset for older browsers
article,
aside,
details,
figcaption,
figure,
footer,
header,
hgroup,
menu,
nav,
section {
  display: block;
}
body {
  line-height: 1;
}
ol,
ul {
  list-style: none;
}
table {
  border-collapse: collapse;
  border-spacing: 0;
}
</style>
