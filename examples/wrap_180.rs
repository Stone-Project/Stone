// stone:job stone:math.wrap_180
// stone:function wrap_180_rs

#[no_mangle]
pub extern "C" fn wrap_180_rs(d: i32) -> i32 {
    let mut r = d.rem_euclid(360);
    if r > 180 {
        r -= 360;
    }
    r
}
