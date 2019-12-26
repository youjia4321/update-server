import axios from 'axios'
import { LoadingBar } from 'view-design';
import qs from 'qs'

const isDev = process.env.NODE_ENV === 'development'

const ajax = axios.create({
    baseURL: isDev ? "http://192.168.1.179:8000" : "http://192.168.1.179:8000"
})


// 拦截器 
ajax.interceptors.request.use((config) => {
    LoadingBar.start();
    return config
})

ajax.interceptors.response.use((resp) => {
    LoadingBar.finish();
    if (resp.status === 200) {
        return resp.data
    }
})

// 用户登录
export const userLogin = (username, password, headers) => {
    return ajax({
        url: '/api/userLogin',
        method: 'post',
        responseType: 'json',
        data: qs.stringify({ 'username': username, 'password': password }),
        headers: {
            'X-CSRFToken': headers
        }
    })
}

// 用户注销
export const userLogout = () => {
    return ajax.get('/api/userLogout')
}

// 修改密码
export const modifyPwd = (user, newPwd, headers) => {
    return ajax({
        url: '/api/modifyPassword',
        method: 'post',
        responseType: 'json',
        data: qs.stringify({ 'user': user, 'newPwd': newPwd }),
        headers: {
            'X-CSRFToken': headers
        }
    })
}

// 选择类型
export const responseType = () => {
    return ajax.get('/api/responseTypes')
}


// 返回指定类型的设备信息
export const responseTypeEquipment = (tag, headers) => {
    return ajax({
        url: '/api/responseEquipments',
        method: 'post',
        responseType: 'json',
        data: qs.stringify({ 'tag': tag }),
        headers: {
            'X-CSRFToken': headers
        }
    })
}


// 返回表格数据
export const responseTable = (tag, headers) => {
    return ajax({
        url: '/api/responseTable',
        method: 'post',
        responseType: 'json',
        data: qs.stringify({ 'tag': tag }),
        headers: {
            'X-CSRFToken': headers
        }
    })
}

export const responseSingleTable = (tag, equipment_id, headers) => {
    return ajax({
        url: '/api/responseSingleTable',
        method: 'post',
        responseType: 'json',
        data: qs.stringify({ 'tag': tag, 'equipment_id': equipment_id }),
        headers: {
            'X-CSRFToken': headers
        }
    })
}

export const changeStatus = (tag, equipment_id, headers) => {
    return ajax({
        url: '/api/changeStatus',
        method: 'post',
        responseType: 'json',
        data: qs.stringify({ 'tag': tag, 'equipment_id': equipment_id }),
        headers: {
            'X-CSRFToken': headers
        }
    })
}



// 创建设备类型 设备信息
export const createTag = (tag, headers) => {
    return ajax({
        url: '/api/createTag',
        method: 'post',
        responseType: 'json',
        data: qs.stringify({ 'tag': tag }),
        headers: {
            'X-CSRFToken': headers
        }
    })
}


export const createEquipment = (tag, equipment_id, headers) => {
    return ajax({
        url: '/api/createEquipInfo',
        method: 'post',
        responseType: 'json',
        data: qs.stringify({ 'tag': tag, 'equipment_id': equipment_id }),
        headers: {
            'X-CSRFToken': headers
        }
    })
}

// 删除
export const deleteGlobalFile = (tag, filename, headers) => {
    return ajax({
        url: '/api/deleteGlobalFile',
        method: 'post',
        responseType: 'json',
        data: qs.stringify({ 'tag': tag, 'filename': filename }),
        headers: {
            'X-CSRFToken': headers
        }
    })
}

export const deleteGlobalFiles = (tag, filelist, headers) => {
    var files = JSON.stringify(filelist)
    return ajax({
        url: '/api/deleteGlobalFiles',
        method: 'post',
        responseType: 'json',
        data: qs.stringify({ 'tag': tag, 'filelist': files }),
        headers: {
            'X-CSRFToken': headers
        }
    })
}

// 编辑
export const editGlobalFile = (tag, filename, headers) => {
    return ajax({
        url: '/api/editGlobalFile',
        method: 'post',
        responseType: 'json',
        data: qs.stringify({ 'tag': tag, 'filename': filename }),
        headers: {
            'X-CSRFToken': headers
        }
    })
}

export const editGlobalFiles = (tag, filelist, headers) => {
    return ajax({
        url: '/api/editGlobalFiles',
        method: 'post',
        responseType: 'json',
        data: ({ 'tag': tag, 'filelist': filelist }),
        headers: {
            'X-CSRFToken': headers
        }
    })
}

// 删除
export const deleteSingleFile = (tag, equipment_id, filename, headers) => {
    return ajax({
        url: '/api/deleteSingleFile',
        method: 'post',
        responseType: 'json',
        data: qs.stringify({ 'tag': tag, 'equipment_id': equipment_id, 'filename': filename }),
        headers: {
            'X-CSRFToken': headers
        }
    })
}

export const deleteSingleFiles = (tag, equipment_id, filelist, headers) => {
    var files = JSON.stringify(filelist)
    return ajax({
        url: '/api/deleteSingleFiles',
        method: 'post',
        responseType: 'json',
        data: qs.stringify({ 'tag': tag, 'equipment_id': equipment_id, 'filelist': files }),
        headers: {
            'X-CSRFToken': headers
        }
    })
}

// 编辑
export const editSingleFile = (tag, equipment_id, filename, headers) => {
    return ajax({
        url: '/api/editSingleFile',
        method: 'post',
        responseType: 'json',
        data: qs.stringify({ 'tag': tag, 'equipment_id': equipment_id, 'filename': filename }),
        headers: {
            'X-CSRFToken': headers
        }
    })
}

export const editSingleFiles = (tag, equipment_id, filelist, headers) => {
    var files = JSON.stringify(filelist)
    return ajax({
        url: '/api/editSingleFiles',
        method: 'post',
        responseType: 'json',
        data: qs.stringify({ 'tag': tag, 'equipment_id': equipment_id, 'filelist': files }),
        headers: {
            'X-CSRFToken': headers
        }
    })

}

// 删除类型

export const deleteType = (tag, headers) => {
    return ajax({
        url: '/api/deleteType',
        method: 'post',
        responseType: 'json',
        data: qs.stringify({ 'tag': tag }),
        headers: {
            'X-CSRFToken': headers
        }
    })
}

export const deleteEquipment = (equipment_id, headers) => {
    return ajax({
        url: '/api/deleteEquipment',
        method: 'post',
        responseType: 'json',
        data: qs.stringify({ 'equipment_id': equipment_id }),
        headers: {
            'X-CSRFToken': headers
        }
    })
}

export const deleteEquipments = (equiplist, headers) => {
    var equipments = JSON.stringify(equiplist)
    return ajax({
        url: '/api/deleteEquipments',
        method: 'post',
        responseType: 'json',
        data: qs.stringify({ 'equipments': equipments }),
        headers: {
            'X-CSRFToken': headers
        }
    })
}

export const responseEquipment = () => {
    return ajax.get('/api/responseEquipment')
}


export const responseTemp = () => {
    return ajax.get('/transform/response/temp')
}