// stone:job stone:math.lerp_angle
// stone:function lerp_angle_rs

#[no_mangle]
pub extern "C" fn lerp_angle_rs(a: f64, b: f64, t: f64) -> f64 {
    const PI: f64 = std::f64::consts::PI;
    let d = (b - a + PI).rem_euclid(2.0 * PI) - PI;
    a + d * t
}
