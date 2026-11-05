// stone:job stone:math.fade
// stone:function fade_rs

#[no_mangle]
pub extern "C" fn fade_rs(t: f64) -> f64 {
    t * t * t * (t * (t * 6.0 - 15.0) + 10.0)
}
