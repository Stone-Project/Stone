// stone:job stone:math.angle_diff_deg
// stone:function angle_diff_deg_rs

#[no_mangle]
pub extern "C" fn angle_diff_deg_rs(a: i32, b: i32) -> i32 {
    let mut d = (b - a + 180).rem_euclid(360) - 180;
    if d == -180 {
        d = 180;
    }
    d
}
