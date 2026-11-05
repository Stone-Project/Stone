// stone:job stone:math.angle_diff
// stone:function angle_diff_rs

#[no_mangle]
pub extern "C" fn angle_diff_rs(a: f64, b: f64) -> f64 {
    const PI: f64 = std::f64::consts::PI;
    (b - a + PI).rem_euclid(2.0 * PI) - PI
}
