// stone:job stone:math.sign
// stone:function sign_rs

#[no_mangle]
pub extern "C" fn sign_rs(value: i32) -> i32 {
    if value < 0 {
        return -1;
    }
    if value > 0 {
        return 1;
    }
    0
}
