// stone:job stone:math.wrap_angle
// stone:function wrap_angle_rs

#[no_mangle]
pub extern "C" fn wrap_angle_rs(a: f64) -> f64 {
    const PI: f64 = std::f64::consts::PI;
    (a + PI).rem_euclid(2.0 * PI) - PI
}
