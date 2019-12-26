import SysHeader from '@/components/SysHeader'
const Login = () => import('@/views/login/SysLogin')
const Index = () => import('@/views/index/SysIndex')
const Reagent = () => import('@/views/reagent/SysReagent')
const ReagentDetail = () => import('@/views/reagent/SysReagentDetail')

const Websocket = () => import('@/views/Websocket')
const upload = () => import('@/views/upload/SysUpload')

export default [
    {
        path: '/',
        redirect: '/system_Index',

    }, {
        path: '/system_Index',
        name: 'systemIndex',
        components: {
            default: Index,
            header: SysHeader
        },
        meta: {
            requireAuth: true
        }

    }, {
        path: '/system_Login',
        name: 'systemLogin',
        components: {
            login: Login,
        }
    }, {
        path: '/system_Reagent',
        name: 'systemReagent',
        components: {
            default: Reagent,
            header: SysHeader
        },
        meta: {
            requireAuth: true
        }
    }, {
        path: '/system_OneReagent',
        name: 'system_reagent',
        components: {
            default: ReagentDetail,
            header: SysHeader
        },
        meta: {
            requireAuth: true
        }
    }, {
        path: "/system_Websocket",
        name: "websocket",
        components: {
            default: Websocket,
        },
        meta: {
            requireAuth: true
        }
    },{
        path: "/system_Upload",
        name: "upload",
        components: {
            default: upload,
            header: SysHeader
        },
        meta: {
            requireAuth: true
        }
    }
]
