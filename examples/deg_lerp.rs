// stone:job stone:math.deg_lerp
// stone:function deg_lerp_rs

#[no_mangle]
pub extern "C" fn deg_lerp_rs(a: f64, b: f64, t: f64) -> f64 {
    let d = (b - a + 180.0).rem_euclid(360.0) - 180.0;
    a + d * t
}
